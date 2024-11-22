import streamlit as st
import data_sets
# Function to display category titles with colors
def styled_title(title, color="skyblue", htmltag ="h3", alignment=""):
    return f"<{htmltag}  style='color:{color}; text-align:{alignment};'>{title}</{htmltag}>"
st.set_page_config(layout="wide")

# Main layout with two columns for image and about info
col1, col2 = st.columns(2)

with col1:
    st.image("images/DiegoPhoto.jpg")

with col2:
    st.markdown(styled_title("Diego Cuellar", color="azure", htmltag="h1", alignment="center"), unsafe_allow_html=True)
    st.markdown(styled_title("About me", color="deepskyblue", htmltag="h2", alignment="center"), unsafe_allow_html=True)

    content = """
    Currently a full-time student at NBCC in the Programmer-Analyst program, expected to graduate in 
    June 2025. I have a strong passion for learning, and I would love to show you some of my skills.
    """
    st.info(content)

    st.markdown(styled_title("Contact Details", color="deepskyblue", htmltag="h2", alignment="center"), unsafe_allow_html=True)


    # Create a container for both Contact Info and Socials
    with st.container():
        # Outer columns for Contact Info and Socials (no nesting columns inside columns)
        col_contact,col_separator,col_socials = st.columns([1.5, 0.5, 1.5])

        # Left column: Contact Information
        with col_contact:
            # st.subheader("Contact Information")
            st.write("Phone: 506-897-0187")
            st.write("Email: diego_cuellar24@hotmail.com")

        # Right column: Socials
        with col_socials:
            # st.subheader("Follow me")
            # Use st.write with markdown to format LinkedIn and GitHub
            # LinkedIn with icon and link in the same line
            st.markdown(
                "<a href='https://www.linkedin.com/in/diego-cuellar24/' target='_blank'><img src='https://raw.githubusercontent.com/YeyoDC/Portfolio/master/images/linkedin.png' width='40' style='vertical-align: middle;' /></a> "
                "<a href='https://www.linkedin.com/in/diego-cuellar24/' target='_blank'>**LinkedIn**</a>",
                unsafe_allow_html=True
            )

            # GitHub with icon and link in the same line
            st.markdown(
                "<a href='https://github.com/YeyoDC' target='_blank'><img src='https://raw.githubusercontent.com/YeyoDC/Portfolio/master/images/github.png' width='40' style='vertical-align: middle;' /></a> "
                "<a href='https://github.com/YeyoDC' target='_blank'>**GitHub**</a>",
                unsafe_allow_html=True
            )
            # st.write("**LinkedIn**: [LinkedIn](https://www.linkedin.com/in/diego-cuellar24/)")
            # st.image("images/linkedin.png", width=40)
            # st.write("**GitHub**: [GitHub](https://github.com/YeyoDC)")
            # # Use st.image for the icons
            # st.image("images/github.png", width=40)

# IT Skills section
st.markdown(styled_title("IT Skills", color="deepskyblue", htmltag="h2", alignment="center"), unsafe_allow_html=True)
# Create 3 columns for layout
cols = st.columns([1.4, 1, 1])

# Track which column the content goes into
col_idx = 0



# Display grouped skills in columns with colored titles
for category, skills_list in data_sets.skills_grouped.items():
    if isinstance(skills_list, dict):  # If the category has subcategories
        with cols[col_idx]:
            st.markdown(styled_title(category, color="lightcyan"), unsafe_allow_html=True)
            for subcategory, subskills in skills_list.items():
                st.markdown(f"**{subcategory}:**")
                st.write(", ".join(subskills))
        col_idx = (col_idx + 1) % 3  # Cycle through columns
    else:
        # Directly display category and skills in the columns
        with cols[col_idx]:
            st.markdown(styled_title(category, color="lightblue"), unsafe_allow_html=True)
            st.write(", ".join(skills_list))
        col_idx = (col_idx + 1) % 3  # Cycle through columns

# Projects section
st.markdown(styled_title("Projects", color="deepskyblue", htmltag="h2", alignment="center"), unsafe_allow_html=True)
project_info = """
Here are some of the projects I have completed at NBCC, which showcases some of the skills I have adquired during the program. 
Make sure you come by regularly as I might have new interesting projects
"""
st.info(project_info)

# Projects layout with two main columns
col3,col_sep, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    st.markdown(styled_title("To do app", color="lightblue", htmltag="h2"), unsafe_allow_html=True)
    st.write("App that allows you to add activities so you remember, and once done they can be deleted")
    st.write("Tools: Python, Streamlit")
    st.image("images/1.png", width=250)
    st.write("[Source Code](https://github.com/YeyoDC/to-do-WebApp)")

    st.markdown(styled_title("Social Media Website", color="lightblue", htmltag="h2"), unsafe_allow_html=True)
    st.write("Social media website that allows you to post what you think in a fun way")
    st.write("Tools: PHP, MySQL, HTML, CSS, Boostrap")
    st.image("images/15.png", width=250)
    st.write("[Source Code](https://github.com/YeyoDC/y-socialMedia)")

with col4:
    st.markdown(styled_title("Students Scores", color="lightblue", htmltag="h2"), unsafe_allow_html=True)
    st.write("App that allows you upload students scores into a list. This uses Object-oriented programming principles")
    st.write("Tools: C#")
    st.image("images/12.png", width=250)
    st.write("[Source Code](https://github.com/YeyoDC/StudentsScore)")

    st.markdown(styled_title("Pet Modeling Photograph", color="lightblue", htmltag="h2"), unsafe_allow_html=True)
    st.write("Website dedicated to attract pets to serve as models for different projects like commercials and movies")
    st.write("Tools: HTML, CSS")
    st.image("images/2.png", width=250)
    st.write("[Source Code](https://github.com/YeyoDC/pet_modeling)")
