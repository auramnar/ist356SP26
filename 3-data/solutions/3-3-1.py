import pandas as pd
import numpy as np
import requests
import streamlit as st

'''for each department:
    #create a dataframe for that department (e.g. from the json under the department)
    #add lineage to the dataframe (e.g. add the department name)
    #add the dataframe to a list of departments
concat the list of departments together one dataframe
print dataframe
'''


link ="https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(link)
employees = response.json()
st.write(employees)

