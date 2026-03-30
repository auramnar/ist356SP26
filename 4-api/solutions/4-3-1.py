'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/genai/generate?model=llama3%3Alatest&temperature=0.7&max_tokens=1000' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 'include_your_api_key_here'' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'query=what%20is%20the%20latest%20temp'

'''

import requests
import streamlit as st

def generate_ai_response(prompt: str) -> str:
    params = {'temperature}
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {"query": prompt}
    headers = {"X-API-KEY": "your_api_key_here"}
    response = requests.post(url, data= data, headers=headers) 
    response.raise_for_status()
    results = response.json()
    return results


  
def spellcheck(text: str) -> str: 
    prompt = f"Spellcheck the following text:"
    prompt += text + "\n"
    prompt += "for each misspelling provide one suggestion"
    check = generate_ai_response(prompt)
    return check
    
# MAIN PROGRAM
st.title("Spellcheck with AI")
text = st.text_area("Enter text to spellcheck:")
s_check = spellcheck(text)
st.write(s_check)

