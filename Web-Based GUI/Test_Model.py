import streamlit as st
import cv2
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow import image
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
cwd = os.getcwd()

try:
    model = load_model(cwd + "/"+"../Model_tf")
except: 
    st.subheader("Error! Saved model 'Model_tf' not found. Make sure it is present in main directory of project: './Image Classifier/'")

class_dic = {0:'Building', 1:'Car', 2:'Dog', 3:'Flower', 4:'Forest',
            5:'Person', 6:'Pizza', 7:'Sea', 8:'Ship', 9:'Traffic Sign'}




def import_and_predict(image_data, model):
    
        size = (150,150)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(150, 150), interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img_resize[np.newaxis,...]

        prediction = model.predict(img_reshape)
        
        return prediction


def app():
    st.header("Image Classifier")

    file = st.file_uploader("Please Upload the Image", type=["jpg", "png"])
        
    if file is None:
        st.write("No Image Selected.")
    else:
        image = Image.open(file)
        st.image(image)
        prediction = import_and_predict(image, model)
        
        st.subheader("Prediction: "+ class_dic[np.argmax(prediction)])