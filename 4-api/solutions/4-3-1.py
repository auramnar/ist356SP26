'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/genai/generate?model=llama3%3Alatest&temperature=0.7&max_tokens=1000' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ec25dc1e1297cfba51838bd3' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'query=what%20is%20the%20latest%20temp'

'''

import requests
import streamlit as st

