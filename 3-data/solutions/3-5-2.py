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


