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

# WRAP OPEN API CALL IN A FUNCTION
def generate_ai_response(query:str) -> str:
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {"query" : query}
    response = requests.post(url, data=data, headers={"X-API-KEY": "your_api_key_here"})
    response.raise_for_status()
    results = response.json()
    return results

# SPELL CHECK FUNCTION 
def spell_check(text:str) -> str:
  prompt ="Spell check the following text"
  prompt += text + "\n"
  prompt += "For each mispelling provide at least one suggestion"
  prompt += "If there are no misspellings, say 'No misspellings found'"
  prompt += "return as a list of dictionaries in JSON format"
  check = generate_ai_response(prompt)
  return check


# MAIN APP
st.title("SPELL CHECKER")
text = st.text_input("Enter text to check:")
s_check = spell_check(text)
st.write(s_check)
