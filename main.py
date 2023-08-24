import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Paul Lennard")
    content = """
    Hi, I am Paul Lennard! I am a data scientist and software developer. I have a passion for creating meaningful and insightful data-driven applications. With a background in computer science and machine learning, I enjoy solving complex problems using Python and various data analysis tools.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])



with col4:
    for index, row in df[:10].iterrows():
        st.header(row["title"])