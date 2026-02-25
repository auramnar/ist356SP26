
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

