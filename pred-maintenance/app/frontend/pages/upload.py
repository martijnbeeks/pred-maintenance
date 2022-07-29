import streamlit as st
import pandas as pd
import os, sys
import requests
import json

p = os.path.abspath('.')
sys.path.insert(1, p)
import config


def search_func(to_check, columns):
    not_present = []
    for i in to_check:
        if i not in columns:
            not_present.append(i)
    return not_present


# @st.cache
def app():
    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file for status prediction.")

    # Code to read a single file
    uploaded_file = st.file_uploader("Choose a file", type=['csv'])
    if not uploaded_file:
        st.write("Upload a .csv file to get started")
        return

    st.write('Data:')
    df = pd.read_csv(uploaded_file, sep=',', index_col=0)
    st.write(df.head(1))

    # Check if all columns are there
    not_present = search_func(config.COLUMNS, df.columns)
    if len(not_present) > 0:
        st.write(f"Columns {not_present} not available")
        return
    else:
        st.write("All columns are available")

    # Post request for prediction
    predict_dict = df.iloc[0].to_json()
    res = requests.post(config.URL, data=predict_dict)
    prediction = json.loads(res.text)
    proba = [float(x) for x in prediction['prediction'].strip('][{}').split(',')]

    st.write(f"Prediction probabilities for uploaded case:")
    st.write(f"Non functional: {round(proba[0],3)}")
    st.write(f"Functional needs repair: {round(proba[1],3)}")
    st.write(f"Functional: {round(proba[2],3)}")