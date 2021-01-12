from os.path import basename
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QPoint, Qt, QRect, QSize
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QPushButton, QMenu, QFileDialog, QStyle
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont, QPixmap
import sys
import SnippingTool
import os
cwd = os.getcwd()


CSS = \
{
    'QWidget':
    {
        'background-color': '#333333',
    },
    'QLabel':
    {
        'color': '#ffffff',
        'background-color': '#333333',
        'font-weight': 'bold',
    },

    'QPushButton':
    {
        'color': 'rgb(255,255,255)',
        'background-color': 'rgb(51,51,51)',
        'font-weight': 'bold',
        'border': '2px solid rgb(51,51,51)',
        'padding': '5px',
    },
    'QPushButton:pressed':
    {
        'border': '2px solid rgb(0,143,150)',
        'background-color': 'rgb(51,51,51)'
    },
    'QPushButton:hover':
    {
        'color': '#85d5ff',
        'border': '2px solid rgb(133, 213, 255)',
        'background-color': 'rgb(133, 213, 255)'
    }
}

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




class Menu(QMainWindow):

    
    def __init__(self):
        super(Menu, self).__init__() 
        self.setStyleSheet(dictToCSS(CSS))
        self.IdentifyImage = SnippingTool.IdentifyImage()
        self.SearchAboutImage = SnippingTool.SearchAboutImage()
        self.CopyTextToClipboard = SnippingTool.CopyTextToClipboard()
        self.initUI()


    def initUI(self):

        self.setObjectName("Image Analyser")
        self.setWindowTitle("What's On My Screen?")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setEnabled(True)
        self.resize(220, 140)
        self.setGeometry(1680,880,220,140)
        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10,0,150,30))
        self.label.setText("What's On My Screen?")
        self.label.setFont(QFont('Arial',8))
        
        self.logo = QtWidgets.QLabel(self)
        self.logo.setPixmap(QPixmap(QIcon(cwd + '/' + 'logo.png').pixmap(QSize(60,60))))
        self.logo.setGeometry(QtCore.QRect(160,100,60,60))

        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(200,0,20,20))
        self.close_button.setObjectName("close_button")
        self.close_button.setIcon(QIcon('C:/Users/gutte/Desktop/College Projects/SDL Projects/Mini Project/close_icon.png'))
        self.close_button.setIconSize(QSize(20,20))
        self.close_button.setToolTip("Close")
        self.close_button.clicked.connect(self.closeEvent)

        self.minimize_button = QtWidgets.QPushButton(self)   
        self.minimize_button.setGeometry(QtCore.QRect(180,0,20,20)) 
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setIcon(QIcon('C:/Users/gutte/Desktop/College Projects/SDL Projects/Mini Project/minimize_icon.png'))
        self.minimize_button.setIconSize(QSize(20,20))
        self.minimize_button.setToolTip("Minimize")
        self.minimize_button.clicked.connect(lambda: self.showMinimized())

        self.identify_image = QtWidgets.QPushButton(self)
        self.identify_image.setGeometry(QtCore.QRect(10, 40, 60, 60))
        self.identify_image.setObjectName("identify_image")
        self.identify_image.setIcon(QIcon('C:/Users/gutte/Desktop/College Projects/SDL Projects/Mini Project/identify_image_icon.png'))
        self.identify_image.setIconSize(QSize(55,55))
        self.identify_image.setToolTip("Identify Image")
        self.identify_image.clicked.connect(self.identify_image_func)
        
        self.search_about_image = QtWidgets.QPushButton(self)
        self.search_about_image.setGeometry(QtCore.QRect(80, 40, 60, 60 ))
        self.search_about_image.setObjectName("search_about_image")
        self.search_about_image.setIcon(QIcon('C:/Users/gutte/Desktop/College Projects/SDL Projects/Mini Project/search_image_icon.png'))
        self.search_about_image.setIconSize(QSize(55,55))
        self.search_about_image.setToolTip("Search About Image")
        self.search_about_image.clicked.connect(self.search_about_image_func)

        self.copy_text_to_clipboard = QtWidgets.QPushButton(self)
        self.copy_text_to_clipboard.setGeometry(QtCore.QRect(150, 40, 60, 60))
        self.copy_text_to_clipboard.setObjectName("copy_text_to_clipboard")
        self.copy_text_to_clipboard.setIcon(QIcon('C:/Users/gutte/Desktop/College Projects/SDL Projects/Mini Project/copy_text.png'))
        self.copy_text_to_clipboard.setIconSize(QSize(55,55))
        self.copy_text_to_clipboard.setToolTip("Copy Text To Clipboard")
        self.copy_text_to_clipboard.clicked.connect(self.copy_text_to_clipboard_func)
        

        self.help = QtWidgets.QPushButton(self)
        self.help.setGeometry(QtCore.QRect(0,120,20,20))
        self.help.setObjectName("help")
        self.help.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_MessageBoxInformation')))
        self.help.setIconSize(QSize(20,20))
        self.help.clicked.connect(self.help_func)
        

        self.show()


    def identify_image_func(self):
        self.IdentifyImage.start()
    
    def search_about_image_func(self):
        self.SearchAboutImage.start()

    def copy_text_to_clipboard_func(self):
        self.CopyTextToClipboard.start()

    def help_func(self):
        msg = QtWidgets.QMessageBox()
        msg.setStyleSheet(dictToCSS(popup_CSS))
        msg.setWindowTitle('HELP')
        msg.setText("Identify Image: After clicking on this button crop the region you wish to identify. A dialogue box will appear with result. \n\nSearch About Image: After clicking on this button crop the region you wish to search about. Browser will open with relevant search results. \n\nCopy Text To Clipboard: After clicking on this button crop the region whose text you wish to copy. You can paste it wherever you wish.")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    
    def closeEvent(self,event):
        self.close()
        sys.exit()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Menu()
    sys.exit(app.exec_())
