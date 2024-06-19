import streamlit as st

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
