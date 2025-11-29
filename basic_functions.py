# refer to the mini app example on the website under Streamlit --> Functions

import streamlit as st

st.title("Streamlit Demo App")
st.header("User Input Section")

st.write("**Please** provide your details *below:*")

age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25,
                      step=1)

color = st.selectbox("Choose your favorite color:",
                      ["Red", "Blue", "Green"],
                      index=1)

if st.button("Submit"):
    st.success(f"## Thank you! Age: {age}, Favorite Color: {color}")
