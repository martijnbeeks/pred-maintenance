import streamlit as st
import numpy as np
from PIL import Image



def app():
    st.markdown("Exploratory analysis")


    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image(np.array(Image.open('images/logo-fastapi.png')), width=75)
    with col2:
        st.image(np.array(Image.open('images/logo-sklearn.png')), width=75)
    with col3:
        st.image(np.array(Image.open('images/logo-streamlit.png')), width=75)
    with col4:
        st.image(np.array(Image.open('images/logo-xgboost.png')), width=75)