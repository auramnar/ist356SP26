'''
Using the `data/mobile_user_behavior_dataset.csv` file, create a streamlit to show:

1. the data in a dataframe 
2. select a category: gender or operating system
3. select a measure: Data useage, battery drain, screen on time, or app useage time
4. show a bar plot of the average of 3. by 2.


'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")
plot, series = plt.subplots()

category = st.selectbox("Select a category:", ["Gender", "Operating System"])
measure = st.selectbox("Select a measure:", ["Data Usage (MB/day)", "Battery Drain (mAh/day)", "Screen On Time (hours/day)", "App Usage Time (minutes/day)"])


st.dataframe(mobile)
sns.barplot(data=mobile,
            x = category,
            y = measure,
            estimator="mean",
            errorbar= None, 
            ax=series).set_title("Average Data Usage")
st.pyplot(plot)      
            
