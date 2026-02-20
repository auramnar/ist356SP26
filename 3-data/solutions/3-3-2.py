import streamlit as st
import pandas as pd
import requests
import numpy as np



base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ['jan', 'feb', 'mar', 'apr'] # list of months to use in a dropdown menu

st.title("Who's not Buying from MiniMart?")
month = st.selectbox('Select Month:', months) # dropdown menu

purchases = pd.read_csv(f"{base}/purchases-{month}.csv") # load file based on month selected
st.dataframe(purchases) # display purchase

# Merge purchases with customers on customet id
# Left join to keep all customers
# Those who did not buy will have a null order id
# We filter for those null order

customers = pd.read_csv(f"{base}/customers.csv")
combined = pd.merge(customers, purchases, left_on='customer_id', right_on= 'customer_id', how='left')
st.dataframe(combined)


cols= ['customer_id', 'firstname', 'lastname'] # select colunms to display
did_not_buy = combined["order_id"].isnull() #return boolean series where true means the customer did not buy anything
customers_who_did_not_buy = combined[did_not_buy][cols] # filter for customers who did not buy and select only the columns we want to display

st.dataframe(customers_who_did_not_buy, hide_index=True) # display customers who did not buy and exclude index

