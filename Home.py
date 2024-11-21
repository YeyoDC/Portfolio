import streamlit as st
import data_sets

st.set_page_config(layout="wide")

# Main layout with two columns for image and about info
col1, col2 = st.columns(2)

with col1:
    st.image("images/DiegoPhoto.jpg")

with col2:
    st.markdown("<h1 style='text-align: center;'>Diego Cuellar</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>About me</h2>", unsafe_allow_html=True)
    content = """
    Currently a full-time student at NBCC in the Programmer-Analyst program, expected to graduate in 
    June 2025. I have a strong passion for learning, and I would love to show you some of my skills.
    """
    st.info(content)

    st.markdown("<h2 style='text-align: center;'>Contact information</h2>", unsafe_allow_html=True)

    # Contact information
    st.subheader("Diego Cuellar")
    st.write("Phone: 5068970187")
    st.write("Email: diego_cuellar24@hotmail.com")

    # Socials layout
    st.subheader("Socials:")
    colsocials = st.columns(2)

    with colsocials[0]:
        st.image("images/linkedin.png", width=40)  # Adjust width to your preferred icon size
        st.write("[LinkedIn](https://www.linkedin.com/in/diego-cuellar24/)")

    with colsocials[1]:
        st.image("images/github.png", width=40)  # Adjust width to your preferred icon size
        st.write("[GitHub](https://github.com/YeyoDC)")

# IT Skills section
st.markdown("<h2 style='text-align: center;'>IT skills</h2>", unsafe_allow_html=True)

# Columns to divide the skills
skill_col_1, skill_col_2, skill_col_3 = st.columns(3)
with skill_col_1:
    skill_list = "".join(f"<li>{skill}</li>" for skill in data_sets.skills[:5])
    st.markdown(f"<ul>{skill_list}</ul>", unsafe_allow_html=True)

with skill_col_2:
    skill_list = "".join(f"<li>{skill}</li>" for skill in data_sets.skills[5:10])
    st.markdown(f"<ul>{skill_list}</ul>", unsafe_allow_html=True)

with skill_col_3:
    skill_list = "".join(f"<li>{skill}</li>" for skill in data_sets.skills[10:])
    st.markdown(f"<ul>{skill_list}</ul>", unsafe_allow_html=True)

# Projects section
st.subheader("Projects:")
st.write("""
Below you can find some of my projects from school that I have been working on:
""")

# Projects layout with two main columns
col3, col4 = st.columns(2)

with col3:
    st.header("To do app")
    st.write("App that allows you to add activities so you remember, and once done they can be deleted")
    st.image("images/1.png")
    st.write("[Source Code](https://github.com/YeyoDC/to-do-WebApp)")

    st.header("Social Media Website")
    st.write("Social media website that allows you to post what you think in a fun way")
    st.image("images/15.png")
    st.write("[Source Code](https://github.com/YeyoDC/y-socialMedia)")

with col4:
    st.header("Students Scores")
    st.write("App that allows you upload students scores, coded in C# using Object-oriented principles")
    st.image("images/12.png")
    st.write("[Source Code](https://github.com/YeyoDC/StudentsScore)")

    st.header("Pet Modeling Photograph")
    st.write("Website dedicated to attract pets to serve as models for different projects like commercials and movies")
    st.image("images/2.png")
    st.write("[Source Code](https://github.com/YeyoDC/pet_modeling)")
