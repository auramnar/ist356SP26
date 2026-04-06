import requests
import json
import pandas as pd 
import streamlit as st

st.title("LLM Spell Checker v2")

text = st.text_area("Enter your text:") # input box 

if st.button("Spell Check"): # run code when button is clicked
    with st.spinner("Searching misspellings..."): # animation to show while waiting
        prompt = ''' # prompt for the LLM to check for spelling errors and suggest corrections.
        I would like you to check input text for spelling errors, suggest corrections, and output the corrected text.
        
        Output must be in a machine-readable format. 
        EXAMPLE 1
        {
            "text": "trhis is a test",
            "corrected-text" : "this is a test",
            "corrections": [
                {
                    "word": "trhis",
                    "correction": "this"
                }
            ]
        }


        EXAMPLE 2
        {
            "text": "I lyke cheez!",
            "corrected-text" : "I like cheese!",
            "corrections": [
                {
                    "word": "lyke",
                    "correction": "like"
                },
                {
                    "word": "cheez",
                    "correction": "cheese"
                }
            ]
        }
        
        Here is the Text to check for spelling errors:
     
        '''
# The prompt above are instructions on what to do and how to format.
# examples are shots to provide guidance. Known as few shot prompting.
# you are controlling the task, JSON output, field names, structure.

        prompt += text # add the user input text to the prompt

        api_key = "your key"
        uri = "https://cent.ischool-iot.net/api/genai/generate"
        data = { "query": prompt }
        response = requests.post(uri, data=data, headers={"x-api-key": api_key})
        response.raise_for_status()
        result = response.json() # convert response to python dictionary
        st.write("RAW LLM RESPONSE:", result ) # show the raw response from the LLM

        #check data returned from API is a string or dictionary
        if isinstance(result, str): # is the result a string
            json_result = json.loads(result) #if a string, convert to dictionary
        elif "response" in result: #check if a dictionary wrapped in the response field
            json_result = json.loads(result["response"]) #convert to dictionary
        else:
            json_result = result # if already a dictionary. Use directly
        
        st.write("CORRECTED TEXT:") # show corrected text 
        st.write(json_result['corrected-text'])
        
        df = pd.DataFrame(result['corrections']) # create dataframe from 
        
        st.write("CORRECTIONS:") # show the corrections in a table
        st.dataframe(df)
        
