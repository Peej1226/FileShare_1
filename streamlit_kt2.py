import streamlit as st
import pandas as pd
import numpy as np
import plotly
# \TrackerCode\src>streamlit run streamlit_kt2.py
st.title('SBCC Kattis Data')
st.header("This pulls data from open.kattis, specifically the top 50 rank data for the Santa Barbara City College students.")
st.markdown("Produced by Patrick J Maher: github.com/Peej1226/")

# TODO link this to where this data is stored
st.sidebar.subheader('Upload a file')
uploaded_file = st.sidebar.file_uploader("Upload a file")
uploaded_file = "https://github.com/Peej1226/FileShare_1/blob/master/Score_Data.csv"

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.info('File successfully uploaded')

    #  this just prints the entire dataframe //   st.write(df)

    columns = list(df.columns)
    columns_sel = st.multiselect('Select columns',columns,['Alex Kohanim', 'Jacob Lee','Trevor Dolin', 'Gina McCaffrey',
                                                           'Austin Keil', 'Cardiac Mangoes', 'Patrick J Maher', 'AO',
                                                           'Dylan Moon', 'CS180 SBCC', 'Jordan Ayvazian',
                                                           'Berkelly Gonzalez', 'Wyatt Spivak', 'Monica Aguilar',
                                                           'Stephen Strenn', 'TJ McGovern', 'Qimin Tao', 'Jaden Baptista',
                                                           'Ethan Stucky'])
    if not columns_sel:
        st.error("Please select at least one name.")
    else:
        df1 = df[columns_sel]
        st.write(df1)

        df2 = df[columns_sel]
        st.line_chart(df2)
