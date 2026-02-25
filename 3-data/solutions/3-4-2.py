'''
In module `check_functions.py`
1. copy over the `detect_whale()` function and tests
2. write function `detect_tipper(tip_pct, tip_pct_75th_pctile, tip_pct_25_pctile)`
    - should return either "light", "heavy" or ""
3. write tests for `detect_tipper()`

in `3-4-2.py`
1. copy the code from `3-4-1.py`
2. Calculate the ntiles using `.quantile()`
3. call the `apply()` function on the row to make new colums `whale` and `tipper`

'''
import pandas as pd
import streamlit as st

from check_functions import clean_currency, detect_whale, detect_tipper

st.title("Dining Check Data")

#load
checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')
st.write("Raw Data")
st.dataframe(checks)

# transformations 
checks['total_amount_of_check_cleaned'] = checks['total amount of check'].apply(clean_currency)
checks['gratuity_cleaned'] = checks['gratuity'].apply(clean_currency)
checks['price_per_item'] = checks['total_amount_of_check_cleaned'] / checks['total items on check']
checks['price_per_person'] = checks['total_amount_of_check_cleaned'] / checks['party size']
checks['items_per_person'] = checks['total items on check'] / checks['party size']
checks['tip_percentage'] = checks['gratuity_cleaned'] / checks['total_amount_of_check_cleaned']
st.write("Transformed Data")
st.dataframe(checks)


# Get KPI boundaries
ppp_75 = checks['price_per_person'].quantile(0.75) # gives me the 75th percentile for price/person
ipp_75 = checks['items_per_person'].quantile(0.75)
tp_75 = checks['tip_percentage'].quantile(0.75)
tp_25 = checks['tip_percentage'].quantile(0.25)


# Calculate the KPIs


# Show metrics