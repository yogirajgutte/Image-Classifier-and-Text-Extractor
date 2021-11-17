import tkinter as tk
import numpy as np
import cv2
from PIL import ImageGrab
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
cwd = os.getcwd()

import webbrowser
import pytesseract
import pyperclip

from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras import models
from tensorflow import image
import numpy as np
import sys

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
class_dic = {0:'Building', 1:'Car', 2:'Dog', 3:'Flower', 4:'Forest',
            5:'Person', 6:'Pizza', 7:'Sea', 8:'Ship', 9:'Traffic Sign'}

try:
    model = models.load_model(cwd + "/" + "../Model_tf")
except:    
    print("Error! Saved model 'Model_tf' not found. Make sure 'Model_tf' folder is present in main directory of project: './Image Classifier/'.")



popup_CSS = \
{
    'QWidget':
    {
        'background-color': '#333333',
    },
    'QLabel':
    {
        'color': '#ffffff',
        'background-color': '#333333',
    },

    'QPushButton':
    {
        'color': 'rgb(255,255,255)',
        'background-color': '#222222',
        'border': '2px solid rgb(0,0,0)',
        'padding': '20px'
    },

    'QPushButton:hover':
    {
        'background-color': '#3d3d3d',
        'border': '2px solid rgb(0,151,151)',
    },

    'QPushButton:pressed':
    {
        'background-color': '#222222',
        'border': '2px solid rgb(0,0,0)'
    },
}
 
def dictToCSS(dictionnary):
    stylesheet = ""
    for item in dictionnary:
        stylesheet += item + "\n{\n"
        for attribute in dictionnary[item]:
            stylesheet += "  " + attribute + ": " + dictionnary[item][attribute] + ";\n"
        stylesheet += "}\n"
    return stylesheet




class SnippingWidget(QtWidgets.QWidget):
    is_snipping = False
    background = True

    def __init__(self, parent=None):
        super(SnippingWidget, self).__init__()
        self.parent = parent
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

    def start(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        SnippingWidget.background = False
        SnippingWidget.is_snipping = True
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        print('Capture the screen...')
        print('Press Esc to abort capture.')
        self.show()

    def paintEvent(self, event):
        if SnippingWidget.is_snipping:
            brush_color = (128, 128, 255, 100)
            lw = 3
            opacity = 0.3
        else:
            # reset points, so the rectangle won't show up again.
            self.begin = QtCore.QPoint()
            self.end = QtCore.QPoint()
            brush_color = (0, 0, 0, 0)
            lw = 0
            opacity = 0

        self.setWindowOpacity(opacity)
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), lw))
        qp.setBrush(QtGui.QColor(*brush_color))
        rect = QtCore.QRectF(self.begin, self.end)
        qp.drawRect(rect)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            print('Quit')
            self.close()
        event.accept()

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    


class IdentifyImage(SnippingWidget):

    def __init__(self, parent=None):
        super(IdentifyImage, self).__init__()

        
    def mouseReleaseEvent(self, event):
        self.close()
        SnippingWidget.is_snipping = False
        QtWidgets.QApplication.restoreOverrideCursor()
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        if x1==x2 or y1==y2:
            print("Error! Snipped image has zero pixels. Try Again.")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('ERROR!')
            msg.setText("Snipped image has zero pixels. Try Again.")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            x = msg.exec_()
        else:
            img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)


            img = image.resize(img,[150,150])
            img = img_to_array(img)
            img = np.expand_dims(img, axis=0)
        
            prediction = model.predict(img)
            print(class_dic[np.argmax(prediction)])
            
            msg = QtWidgets.QMessageBox()
            msg.setStyleSheet(dictToCSS(popup_CSS))
            msg.setWindowTitle('RESULT:')
            msg.setFont(QFont('Cambria', 14))
            msg.setText(class_dic[np.argmax(prediction)])
            msg.setIcon(QtWidgets.QMessageBox.Information)
            
            x = msg.exec_()

        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        brush_color = (0, 0, 0, 0)
        lw = 0
        opacity = 0




class SearchAboutImage(SnippingWidget):

    def __init__(self, parent=None):
        super(SearchAboutImage, self).__init__()

        
    def mouseReleaseEvent(self, event):
        self.close()
        SnippingWidget.is_snipping = False
        QtWidgets.QApplication.restoreOverrideCursor()
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        if x1==x2 or y1==y2:
            print("Error! Snipped image has zero pixels. Try Again.")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('ERROR!')
            msg.setText("Snipped image has zero pixels. Try Again.")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            x = msg.exec_()
        else:
            img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

            img = image.resize(img,[150,150])
            img = img_to_array(img)
            img = np.expand_dims(img, axis=0)
        
            prediction = model.predict(img)
            search_key = class_dic[np.argmax(prediction)]

            search_key = search_key.replace(' ', '+')
            
            webbrowser.open("https://www.google.com/search?q=" + search_key + "&start=1")

        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        brush_color = (0, 0, 0, 0)
        lw = 0
        opacity = 0

    



class CopyTextToClipboard(SnippingWidget):

    def __init__(self, parent=None):
        super(CopyTextToClipboard, self).__init__()
        
    def mouseReleaseEvent(self, event):
        self.close()
        SnippingWidget.is_snipping = False
        QtWidgets.QApplication.restoreOverrideCursor()
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        if x1==x2 or y1==y2:
            print("Error! Snipped image has zero pixels. Try Again.")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('ERROR!')
            msg.setText("Snipped image has zero pixels. Try Again.")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            x = msg.exec_()
        else:
            img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

        
            # experimental code for converting the image to grayscale
            # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            # gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            # gray = cv2.bitwise_not(img_bin)

            # kernel = np.ones((2, 1), np.uint8)
            # img = cv2.erode(gray, kernel, iterations=1)
            # img = cv2.dilate(img, kernel, iterations=1)


            try:
                pytesseract.pytesseract.tesseract_cmd = cwd + '/' + './Tesseract-OCR/tesseract.exe'
                text = pytesseract.image_to_string(img)
                pyperclip.copy(text)

                msg = QtWidgets.QMessageBox()
                msg.setStyleSheet(dictToCSS(popup_CSS))
                msg.setWindowTitle('RESULT:')
                msg.setText("Text Copied!")
                msg.setIcon(QtWidgets.QMessageBox.Information)

                x = msg.exec_()
            except:
                print("Error! 'tesseract.exe' not found. Make sure 'Tesseract-OCR' folder is present in current working directory.")
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR!')
                msg.setText("'tesseract.exe' not found. Make sure 'Tesseract-OCR' folder is present in current working directory.")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                x = msg.exec_()


        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        brush_color = (0, 0, 0, 0)
        lw = 0
        opacity = 0
