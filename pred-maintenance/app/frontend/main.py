# import requests
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from pages import upload, home, analysis
from PIL import Image
import numpy as np


display = Image.open('images/logo.png')
display = np.array(display)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(display, width=200)
with col3:
    st.write(' ')

st.markdown("<h4 style='text-align: center; color: white;'>Predictive maintenance for waterpumps in Tanzania</h4>", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,  # required
    options=["Home", "Predict", "Analysis"],  # required
    icons=["house", "cloud-upload", "envelope"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

if selected == "Home":
    home.app()
if selected == "Predict":
    upload.app()
if selected == "Analysis":
    analysis.app()