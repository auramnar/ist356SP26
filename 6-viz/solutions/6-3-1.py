import pandas as pd
import streamlit as st
import folium
import streamlit_folium as sf


days  = {
    'Sunday': 'red',
    'Monday': 'orange',
    'Tuesday': 'beige',
    'Wednesday': 'green',
    'Thursday': 'blue',
    'Friday': 'purple',
    'Saturday': 'gray'
}

st.title('Streamlit Park magic')

