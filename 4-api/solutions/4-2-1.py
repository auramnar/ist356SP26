'''
Post curl here
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/azure/entityrecognition' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 'your own key' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=pizza%20is%20good%20not%20customer%20service'


'''



import pandas as pd
import numpy as np
import streamlit as st
import requests
import json 


def extract_entities(text:str) -> dict:
  '''Extract entities from text using Azure Entity Recognition API.'''

#Complete function
  url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
  data = {
        "text": text}
  headers = {
        "accept": "application/json",
        "X-API-KEY": "632985c9646a0bc8f547f1d9"}
  response = requests.post(url, data=data, headers=headers)
  response.raise_for_status()
  return response.json()

#text = "I like sunny days in Syracuse, but I don't like the rain in Seattle."
#result = extract_entities(text) 
#entities = result['results']['documents'][0]['entities']
#st.write(result)
#st.write(entities)
#df = pd.DataFrame(entities)
#st.dataframe(df)

text = st.text_input("Enter text to extract entities from:")
if st.button("Extract Entities"):
  if text:
    result = extract_entities(text) # assign function to text variable
    entities = result['results']['documents'][0]['entities'] # extract entities from json response
    df = pd.DataFrame(entities)
    st.dataframe(df)