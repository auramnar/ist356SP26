'''
https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv

Let's build an interactive pivot table in streamlit!

- create a row and column selection widgets allowing the user to select one of the following columns:  
`'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade'`
- create a measure column selection widget which allows the user to select one of these columns:  
`'Completion_Time','Student_Score'`
- build the pivot table dataframe from the inputs. use the average for the `aggfunc`
- display the pivot table!

'''


import pandas as pd
import streamlit as st


url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv"
exams = pd.read_csv(url)
st.write("Raw Exam Scores Data")
st.dataframe(exams)

cols = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
measures = ['Completion_Time','Student_Score']

row_select = st.selectbox('Select Row', cols)
cols.remove(row_select) # remove the row selection from the column options
col = st.selectbox('Select Column', cols)
value = st.selectbox('Select Measure', measures)

pivot_df = exams.pivot_table(index =row_select, columns=col, values=value, aggfunc='mean')

st.write("Pivot Table")
st.dataframe(pivot_df)  
