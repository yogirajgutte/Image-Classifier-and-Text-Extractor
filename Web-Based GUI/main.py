import streamlit as st
import visualization
import Test_Model
import About_Us
import Main_Page


PAGES = {
    "Main Page": Main_Page,
    "Data Visualization": visualization,
    "Model Testing": Test_Model,
    "About Us": About_Us,   
}


st.sidebar.title("Navigation")

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()