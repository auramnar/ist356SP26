'''
- Build a data pipeline to read in the roster and poll responses then create this dataset:
    - student information
    - date of polling session
    - number of polls during session
    - number of polls student answered during session
    - label indicating if the student was absent or non participant

- streamlit UI where you can select a student and see their polling data and grade

- from the dataset, generate a CSV file for upload into for X-Menboard LMS:
    - one row per student
    - total class sessions
    - total absences AB
    - total non-participant np
    - pct of sessions AB or np
    
    

# Load the roster  
base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls"
roster_df = pd.read_csv(f"{base}/roster.csv")
st.dataframe(roster_df)


-Extract 
-Transform 
-Load

'''

import pandas as pd
import streamlit as st

def grade_attendance(participation: float) -> str:
    '''Return a grade based on the number of polls a student participated'''
    if participation == 0.0:
        return 'AB'
    elif participation < 0.5:
        return 'np'
    else:
        return '+'


# Extract roster
roster_url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/roster.csv"
roster_df = pd.read_csv(roster_url)
st.write("Roster Data")
st.dataframe(roster_df)

# Extract each poll responses
# Add lineage to each poll by adding a date column
polls = [] # create an empty list to hold the poll dataframes
dates =["2024-01-08", "2024-01-15", "2024-01-22", "2024-01-29"]
for date in dates: # loop runs once for each date in the dates list
# Using f string to create the url for each poll based on the date  
    poll = f"https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/poll-responses-{date}.csv"
    
    poll_df = pd.read_csv(poll)
    st.write(f"Poll Data for {date}")
    st.dataframe(poll_df)
    
    poll_df['date'] = date #add lineage to each poll by adding a date column
    polls.append(poll_df) #append to polls list
    st.write(f"Poll Data for {date} with Date Column")
    st.dataframe(poll_df)

# TODO:
# Combine all the poll responses into one dataframe


# TODO:
# Transformation 
# Join the poll responses to the roster

# TODO:
# Determine the max poll count for each date using a pivot table

# TODO:
# Count the number of responses by date for each student using a pivot table. 
# Use fillna(0) to replace any missing values with 0 since if there is no response.

# TODO:
# We now need to create a new dataframe where we will convert the number of polls answered into a grade.
# copy student_responses to a new dataframe.
# Here is an example ...

'''
student_responses2 = student_responses.copy() # copy() ensures we don't overwrite the original student_responses dataframe
# change student poll responses to percentages
for col in student_responses2.columns:
    student_responses2[col] = student_responses2[col] / poll_counts.loc[col, 'poll_num']
# student_responses2[col]. This line accesses the column in the student_responses2 dataframe 
# poll_counts.loc[col, 'poll_num'] means
Look in poll_counts
Find the row with index col
Get the value from column 'poll_num'
Change the poll responses to percentages
'''
# TODO:
# Apply the a grade attendance function that return a grade based on the number of polls a student participated
# You will replace every original data point in copied responses by the output of grade_attendance function when applied to values.
# The percentages will be converted to grades
# display the dataframe

# TODO:
# Make a copy of this dataframe with the grades
# Calculate the total sessions
# display the dataframe

# TODO:
# use row.value_counts() to count the number of AB and np in each row
# Use lambda function to apply this to each row and create new columns for AB and np counts
# Store these counts in new columns in the dataframe
# if AB or np is not present, return 0. Use the get() function to do this.
# Calculate the percentage of sessions that are AB or np
# display this summary dataframe

# TODO:
# merge summary with roster to get student names
# use the netid column from roster_df and the index from summary dataframe to merge

# TODO:
#create a download button. define MIME type to be downloaded is a csv file