#  Challenge 2-2-2
'''
- Import streamlit 
- Initialize session state variables - total, amount and history
- Create title 
- Add input widget
- Create 2 buttons Add to Total → adds amount to history and Clear
- When add button is clicked. Add amount to history and total using sum 
- Display current total, loop through history and print each item
- Display a running list of added amounts.  

'''



import streamlit as st

if 'total' not in st.session_state:
    st.session_state.total = 0
if 'amount' not in st.session_state:
    st.session_state.amount = 0
if 'history' not in st.session_state:
    st.session_state.history = []
    
st.title("Running Total Adder")
# inputs 
amount = st.number_input("Enter an amount to add:", value = st.session_state.amount)
btn_add = st.button("Add to Total")
btn_clear = st.button("Clear")


# add amount to total and history
if btn_add:
    st.session_state.history.append(amount)
    st.session_state.total = sum(st.session_state.history)
    st.write(f"Current Total: {st.session_state.total}")
    st.write("History of Added Amounts:")
    for h in st.session_state.history:
        st.write(f"- {h}")  
        
if btn_clear:
    st.session_state.total = None
    st.session_state.amount = None
    st.session_state.history = []
    st.write(f"st.session_state.history: {st.session_state.history}")
    st.rerun()
