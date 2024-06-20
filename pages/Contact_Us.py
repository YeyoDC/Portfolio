import streamlit as st
import email

st.header("Contact us")

with st.form(key="my_form"):
    user_email = st.text_input("Enter your email")
    message = st.text_area("Your message")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        message = message + user_email
        

