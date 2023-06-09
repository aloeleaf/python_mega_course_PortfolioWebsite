import streamlit as st
import pandas

st.set_page_config(layout="wide")
st



col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("My names")
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
    in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
    pariatur. Excepteur sint occaecat cupidatat non proident,
    sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
    st.info(content)

contact = """
Bellow you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(contact)

col3, col4 =st.columns(2)


df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])