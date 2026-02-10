import streamlit as st

if 'length' not in st.session_state:
    st.session_state.length = 0
if 'width' not in st.session_state:
    st.session_state.width = 0
    
#Initialize 
st.title("Area and Perimeter of a Rectangle")
length = st.number_input("Enter the length of the rectangle:", value = st.session_state.length)
width = st.number_input("Enter the width of the rectangle:", value = st.session_state.width)
btn_clicked =st.button("Calculate Area and Perimeter")
btn_clear = st.button("Clear")

# Checks when clicked
if btn_clicked:
    area = length * width
    perimeter = 2 * (length + width)
    st.write(f"The area of the rectangle is: {area}")
    st.write(f"The perimeter of the rectangle is: {perimeter}")

# reset by clearing
if btn_clear:
    st.session_state.length = None
    st.session_state.width = None
    st.rerun()
    
    







