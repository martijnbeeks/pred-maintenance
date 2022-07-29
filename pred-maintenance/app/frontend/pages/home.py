import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np


# @st.cache
def app():
    # Title of the main page
    st.markdown(
        """This web application provides an interface to a predictive maintenance model 
        for water pumps in Tanzania. A user can upload pump data in the tab "Predict" to this 
        system and can retrieve a prediction including probabilities for this data. The current model supports labels: 
        functional, non-functional and functional-but-in-need-of-repair and requires a fixed set of 
        features."""
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(np.array(Image.open('images/logo-fastapi.png')), width=75)
    with col2:
        st.image(np.array(Image.open('images/logo-sklearn.png')), width=75)
    with col3:
        st.image(np.array(Image.open('images/logo-streamlit.png')), width=75)
    with col4:
        st.image(np.array(Image.open('images/logo-xgboost.png')), width=75)