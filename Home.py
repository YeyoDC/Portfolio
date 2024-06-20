import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/DiegoPhoto.jpg")
with col2:
    st.title("Diego Cuellar")
    content = """
    Hi, I am Diego, I am a python student, I am trying to learn python
     and you will see all my applications on here
    """
    st.info(content)
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me
"""
# writing the content outside of the column
st.write(content2)
# adding new columns
col3, empty_colum, col4 = st.columns([1.5, 0.5, 1.5])

# this will set up the file and save content into df variable
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write("[Source Code](https://pythonhow.com)")
with col4:
    for index, row in df[11:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write("[Source Code](https://pythonhow.com)")

