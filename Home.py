import streamlit as st
import pandas
import data_sets

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/DiegoPhoto.jpg")
with col2:

    st.markdown("<h1 style='text-align: center;'>Diego Cuellar</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>About me</h2>", unsafe_allow_html=True)

    content = """
    Currently a full-time student at NBCC in the Programmer-Analyst program, expected to graduate in 
June 2025. I have a strong passion for learning, and I would love to show you some of my skills
    """
    st.info(content)

    st.markdown("<h2 style='text-align: center;'>IT skills</h2>", unsafe_allow_html=True)
    # Columns to divide the skills
    skill_col_1 , skill_col_2, skill_col_3 = st.columns(3)
    with skill_col_1:
        list = ""
        for skill in data_sets.skills[:5]:
            list += "<li>" + skill +"</li>"
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




# adding new columns
# col3, empty_colum, col4 = st.columns([1.5, 0.5, 1.5])
#
# # this will set up the file and save content into df variable
# df = pandas.read_csv("data.csv", sep=";")
# with col3:
#     for index, row in df[:10].iterrows():
#         st.header(row["title"])
#         st.write(row["description"])
#         st.image(f"images/{row['image']}")
#         st.write("[Source Code](https://pythonhow.com)")
# with col4:
#     for index, row in df[11:].iterrows():
#         st.header(row["title"])
#         st.write(row["description"])
#         st.image(f"images/{row['image']}")
#         st.write("[Source Code](https://pythonhow.com)")

