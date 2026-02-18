'''
Create a streamlit with a histogram of the calories column in the fast food dataset.

`fast_food_nutrition_cleaned.csv` 

the input is the number of bins as a slider. between 1 and 100 bins.

What happens to the data shape when you increase the number of bins?

'''

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


