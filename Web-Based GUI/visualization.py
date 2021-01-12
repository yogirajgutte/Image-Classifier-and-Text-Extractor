import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px



@st.cache()
def load_train_val_data():
    df = pd.read_csv("./data/Training_Validation_Dataset.csv")
    return df

@st.cache()
def load_model_stats():
    df = pd.read_csv("./data/Model_stats.csv", usecols=['Epoch', 'Val_Accuracy'])
    return df

@st.cache()
def load_vgg19_stats():
    df = pd.read_csv("./data/VGG19_Stats.csv", usecols=['Epoch', 'Val_Accuracy'])
    return df

@st.cache()
def load_accuracy():
    df = pd.read_csv("Accuracy.csv")
    return df

def visualize_Training_and_validation_data():
    st.header("Dataset Breakdown")
    df = load_train_val_data()
    layout = go.Layout(
                    title= "<b>Dataset Breakdown</b>",
                    xaxis= dict(title='Category',linecolor='white',),
                    yaxis= dict(title='No. of Samples',linecolor='white'),
                    template="plotly_dark")

    fig = go.Figure(data=[go.Bar(
        name = 'Training Set',
        x = df['Category'],
        y = df['No. of Training Samples'],),
        go.Bar(
            name='Validation Set',
            x = df['Category'],
            y = df['No. of Validation Samples'])],
            layout = layout)
    st.plotly_chart(fig)
    st.write("Above illustration shows the number of samples belonging to each category for both, the training set and validation set. The validation set contains about 20% - 30% samples of corresponding categories of whole dataset.")


def visualize_Model_stats():
    st.header("Model Training Stats")
    df = load_model_stats()
    layout = go.Layout(
                    title= "<b>Original Model</b>",
                    xaxis= dict(title='Epoch',linecolor='white'),
                    yaxis= dict(title='% Validation Accuracy',linecolor='white'),
                    template="plotly_dark",)

    fig = go.Figure(data=[go.Scatter(
        name = 'Training Set',
        x = df['Epoch'],
        y = df['Val_Accuracy'],
        mode='lines+markers',
        line=dict(color='#fc9003'))],
            layout = layout,
            )
    st.plotly_chart(fig)
    st.write("Above illustration shows the validation accuracy of original model for each epoch while training.")
    st.write(" ")
    st.write(" ")
    st.write(" ")


def visualize_VGG_stats():
    st.header("Transfer Learning Stats")
    df = load_vgg19_stats()
    layout = go.Layout(
                    title= "<b>Transfer Learning Model</b>",
                    xaxis= dict(title='Epoch', linecolor='white'),
                    yaxis= dict(title='% Validation Accuracy', linecolor='white'),
                    template="plotly_dark")

    fig = go.Figure(data=[go.Scatter(
        name = 'Training Set',
        x = df['Epoch'],
        y = df['Val_Accuracy'],
        mode='lines+markers',
        line=dict(color='#fcba03'))],
            layout = layout)
    st.plotly_chart(fig)
    st.write("Above illustration shows the validation accuracy of transfer learning model based on VGG19 for each epoch while training.")
    


def visualize_accuracy():
    st.header("Model Testing Stats")
    df = load_accuracy()
    layout = go.Layout(
                    title= "<b>Model Testing Accuracy</b>",
                    xaxis= dict(title='Model', linecolor='white'),
                    yaxis= dict(title='% Accuracy',range=[1,100],linecolor='white'),
                    template="plotly_dark")

    fig = go.Figure(data=[go.Bar(
        name = 'Testing Accuracy',
        x = ['Original Model', 'Transfer Learning (VGG19)'],
        y = df['Accuracy'],
        width= .3)],
            layout = layout)
    st.plotly_chart(fig)
    st.write("Above illustration shows the classification accuracy for original model and the transfer learning model. They were tested against a small test set containing 20 images of each category. Original Model has accuracy of 58% while the transfer learning model has accuracy of 89%.")




# # """Hide in production"""
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# # """Hide in production"""

def app():
    st.title("Data Visualization")
    st.subheader("Select a graph to visualize")
    selectgraph = st.selectbox(
        " ",
        ("<NONE>","Dataset Breakdown", "Model Training Stats", "Model Testing Stats")
    )

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if selectgraph=="<NONE>":
        st.write("No Graph Selected")
    if selectgraph=="Dataset Breakdown":
        visualize_Training_and_validation_data()
    if selectgraph=="Model Training Stats":
        visualize_Model_stats()
        visualize_VGG_stats()
    if selectgraph == "Model Testing Stats":
        visualize_accuracy()


 

