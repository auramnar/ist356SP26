
'''
Let's plot calories vs. sodium broken down by the type fast food restaurant.

Create a streamlit to allow the user to select two restaurants to compare.

Which restaurant is the worst?


'''

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ff = pd.read_csv("./6-viz/data/fast_food_nutrition_cleaned.csv")
print(ff.columns)



