import streamlit as st

st.title("Saying Hello")

name = "test"
st.write(f'Name is {name}')
name = st.text_input("And you are?")

if name:
    st.write(f"Hello, {name}!")
else:
    st.write("Please enter your name above.")