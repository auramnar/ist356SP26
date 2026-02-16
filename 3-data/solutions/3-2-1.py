import pandas as pd
import streamlit as st

st.title("Webtraffic Data")



link = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log'

wt= pd.read_csv(link, sep='\s+',skiprows=3,header=0)
st.dataframe(wt)