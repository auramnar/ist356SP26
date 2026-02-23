'''
1. create a module `check_functions.py`
    - add the `clean_currency()` function definition to it.
    - under `if __name__=='__main__':` add the tests
    - run the code to make sure it works.
2. create your challenge file `3-4-1.py`
    - import streamlit, pandas and your clean_currency function
    - load the checks dataset into a dataframe: 
    - clean the `total amount of check` and `gratuity` columns
    - calculate the `price_per_item`  as total amount of check / total items on check
    - calculate the `price_per_person` as total amont of check / party size
    - calculate the `items_per_person` as total items on check / party size
    - calculate the `tip_percentage` as the total amount of  gratuity/total amount of check
    - display dataframe
    - describe dataframe
    

checks dataset `https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv`

'''
# import streamlit, pandas and your clean_currency function
import pandas as pd 
import streamlit as st
from check_functions import clean_currency

# load the checks dataset into a dataframe
url = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv'
checks = pd.read_csv(url)
st.write("Raw Data")
st.dataframe(checks)

