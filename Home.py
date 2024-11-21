import streamlit as st
import pandas
import data_sets

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/DiegoPhoto.jpg", width=500)
with col2:

    st.markdown("<h1 style='text-align: center;'>Diego Cuellar</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>About me</h2>", unsafe_allow_html=True)

    content = """
    Currently a full-time student at NBCC in the Programmer-Analyst program, expected to graduate in 
June 2025. I have a strong passion for learning, and I would love to show you some of my skills
    """
    st.info(content)
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


st.markdown("<h2 style='text-align: center;'>IT skills</h2>", unsafe_allow_html=True)

# Columns to divide the skills
skill_col_1 , skill_col_2, skill_col_3 = st.columns(3)
with skill_col_1:
    list = ""
    for skill in data_sets.skills[:5]:
        list += "<li>" + skill + "</li>"
    st.html(list)
with skill_col_2:
    list = ""
    for skill in data_sets.skills[5:10]:
        list += "<li>" + skill + "</li>"
    st.html(list)
with skill_col_3:
    list = ""
    for skill in data_sets.skills[10:]:
        list += "<li>" + skill + "</li>"
    st.html(list)

