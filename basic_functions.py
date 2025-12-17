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

name = st.text_input("Enter your name:")

with st.form ("user_form"):
  name2 = st.text_input("Enter your name")
  age2 = st.number_input("Enter your age",
                         min_value = 0,
                         max_value = 100,
                         value = 25,
                         step = 1)
  submitted = st.form_submit_button("Submit")

if submitted:
  st.write(f"Hello {name}, you are {age} years old.")

if st.button("Submit"):
    st.success(f"Thank you! Age: {age}, Favorite Color: {color}, Name: {name}")
