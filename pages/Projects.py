import streamlit as st
import email
import sent_email as gmail


st.subheader("Projects:")
content2 = """
Below you can find some of my projects from school that I have been working on
"""

# writing the content outside of the column
st.write(content2)
# adding new columns
col3, middle_column, col4 = st.columns([1.5, 0.5, 1.5])
with col3:
    st.header("To do app")
    st.write("App that allows you to add activities so you remember, and once done they can be deleted")
    st.image("images/1.png")
    st.write("[Source Code](https://github.com/YeyoDC/to-do-WebApp)")

    st.header("Social Media Website")
    st.write("Social media website, that allows you to post what you think in a fun way")
    st.image("images/15.png")
    st.write("[Source Code](https://github.com/YeyoDC/y-socialMedia)")

with col4:
    st.header("Students Scores")
    st.write("App that allows you upload students scores, coded in c# using Object-oriented principles")
    st.image("images/12.png")
    st.write("[Source Code](https://github.com/YeyoDC/StudentsScore)")

    st.header("Pet Modeling Photograph")
    st.write("Website dedicated to attract pets to serve as models for different projects like commercials and movies")
    st.image("images/2.png")
    st.write("[Source Code](https://github.com/YeyoDC/pet_modeling)")






