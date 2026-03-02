
'''
Create a streamlit to allow the user to select one of the following:

- one of: Made_Own_Study_Guide, Did_Exam_Prep Assignment, Studied_In_Groups	
- after the selection is made display a dataframe that summarized the count of students and the average student score by the selection

'''

import pandas as pd
import streamlit as st


st.title ('Exam Scores Summary')


url ='https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv'
exams = pd.read_csv(url)
st.write("Raw Exam Scores Data")
st.dataframe(exams)

options = ['Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups']
selection = st.selectbox('Select a Study Approach', options)

# group by the option
# reset the index to turn the groupby object into a dataframe
# rename the columns to be more descriptive
# average the student score in each group

summary = exams.groupby(selection).agg({'Class_Section': 'count', 'Student_Score': 'mean'})
summary = summary.reset_index()
summary = summary.rename(columns={'Class_Section': 'Student_Count', 'Student_Score': 'Average_Score'})


st.write(f"Summary of Exam Scores by {selection}")
st.dataframe(summary)