import streamlit as st
from code_helper import run_python_script


st.title("Playwright with Streamlit")

url = st.text_input("Enter a URL")
if url:
    with st.spinner("Scraping..."):
        html_content = run_python_script("5-web/solutions/get-page-text.py", url)
        st.write(html_content)  