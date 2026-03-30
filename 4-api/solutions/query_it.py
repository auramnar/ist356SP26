import pandas as pd
import requests
import streamlit as st

APIKEY = "your_api_key_here"
st.title("Query It")

file = st.file_uploader("Upload a CSV file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    
    # message sent to the AI model. This builds the prompt 
    # use += to add to the prompt in pieces
    question = st.text_input("Enter a question to ask about the data:")
    if question: # only run if there is a question
        prompt = 'With the following data:\n'
        prompt += df.to_string(index=False) # convert dataframe to text form (no row numbers),
        prompt += "\n\n" # add spacing
        prompt += "Answer the following question:\n"  # add the question to the prompt
        prompt += question # add the question to the prompt
        
        url = "https://cent.ischool-iot.net/api/genai/generate"
        response = requests.post(url, data={"query": prompt}, headers={"X-API-KEY": APIKEY}) 
        response.raise_for_status()
        results = response.json()
        st.write(results)  