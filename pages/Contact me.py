import streamlit as st
import email
import sent_email as gmail
st.title("Contact information: ")
st.subheader("Diego Cuellar")
st.write("Phone: 5068970187")
st.write("Email: diego_cuellar24@hotmail.com")
st.write("You can also find me on:")
# Display the LinkedIn icon as a smaller size
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("images/linkedin.png", width=40)  # Adjust width to your preferred icon size
    st.write("[LinkedIn](https://www.linkedin.com/in/diego-cuellar24/)")
with col2:
    st.image("images/github.png", width=40)  # Adjust width to your preferred icon size
    st.write("[github](https://github.com/YeyoDC)")

st.header("Send me a message")

with st.form(key="my_form"):
    user_email = st.text_input("Enter your email")
    raw_message = st.text_area("Your message")
    message = f"""\
    Subject: New email from {user_email}
    
    From: {user_email}
    {raw_message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        gmail.send_email(message, user_email)
        st.info("Your email was sent succesfully")


