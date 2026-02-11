import streamlit as st

st.title("The Memory Box Counter")

# 1. Create the box if it doesn't exist yet
if "clicks" not in st.session_state:
    st.session_state["clicks"] = 0
    st.write("I just set up a new memory box!")

# 2. Make a button to change the memory
if st.button("Tap me!"):
    st.session_state["clicks"] += 1

# 3. Show what's inside the memory box
st.write(f"The computer remembers that you tapped the button **{st.session_state['clicks']}** times.")