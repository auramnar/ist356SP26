'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/genai/generate?model=llama3%3Alatest&temperature=0.7&max_tokens=1000' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: d7bfb0c4cd88d3cf1581c1b2' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'query=why%20do%20tree%20grow%20upwards%3F'

'''


import requests
import streamlit as st

def generate_ai_response(query:str) -> str:
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {"query" : query}
    response = requests.post(url, data=data, headers={"X-API-KEY": "d7bfb0c4cd88d3cf1581c1b2"})
    response.raise_for_status()
    results = response.json()
    return results



st.title("First GPT App")
text = st.text_input("Ask a question to the AI model:")
response = generate_ai_response(text)
st.write(response)