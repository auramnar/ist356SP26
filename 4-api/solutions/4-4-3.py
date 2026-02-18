import streamlit as st  
import requests

url = "http://localhost:8000/tldr"

st.title("AI Text Summarizer")
text = st.text_area("Enter text to summarize")

