import streamlit as st
import pandas as pd
import numpy as np
DATA_URL =("location of file")

st.title("enter title")
st.markdown("")

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['envvar', 'envvar']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)

if st.checkbox("Show Raw Data", False):
   st.subheader('Raw Data')
   st.write(data)
