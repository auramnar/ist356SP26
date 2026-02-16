'''
- Create title
- Define the dataset URL
- Download the JSON data
- Display the raw JSON
- Convert JSON to a DataFrame (First Attempt)
- Convert JSON to a DataFrame (First Attempt)
'''

import requests
import json
import pandas as pd
import streamlit as st

st.title("Employee JSON")

link = "https://raw.githubusercontent.com/mafudge/datasets/master/json-samples/employees.json"
response = requests.get(link)

