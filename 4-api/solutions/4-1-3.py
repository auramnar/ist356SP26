'''
Geocodes 

curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=syracuse%20university' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ec25dc1e1297cfba51838bd3'
  
  
  
  Weather
  
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/weather/current?units=imperial%20&lon=-76&lat=43' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ec25dc1e1297cfba51838bd3'


'''


import pandas as pd
import numpy as np  
import requests
import json

import streamlit as st










