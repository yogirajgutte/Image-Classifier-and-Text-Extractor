import streamlit as st
from string import ascii_uppercase, digits
from random import choices

def app():
    st.title("About Us")
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')


    with st.beta_container():
        column = st.beta_columns(3)

        column[0].image("./data/yogiraj.png")
        column[0].header("Yogiraj Gutte")
        column[0].write("3rd Year, Computer Engineering")
        column[1].write("      ")
        column[2].image("./data/aasit.png")
        column[2].header("Aasit Vora")
        column[2].write("3rd Year, Computer Engineering")