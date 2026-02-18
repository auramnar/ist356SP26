import streamlit as st
import pandas as pd
import requests
import numpy as np



base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ['jan', 'feb', 'mar', 'apr']

customers = pd.read_csv(f"{base}/customers.csv")
st.dataframe(customers)

