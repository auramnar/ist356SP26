import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")
#mobile.columns = ["user_id", "device_mode"....] # snake case to make it easier to work with    
st.dataframe(mobile)

category = st.selectbox("Select Category", 
                        ["Age"])
quantity = st.selectbox("Select Measure", 
                        ["Data Usage (MB/day)", "Battery Drain (mAh/day)", "Screen On Time (hours/day)", "App Usage Time (min/day)"])

figure,series1 =plt.subplots()

sns.lineplot(data=mobile, 
             x=category, 
             y=quantity, 
             estimator= 'mean', 
             errorbar=None,
             ax=series1)
st.pyplot(figure)