import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")


age=st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}.")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")


data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv") # to have a csv file for next operation 
st.write(df)

upload_file = st.file_uploader("Choose the csv file", type="csv")

if upload_file is not None:
    df = pd.DataFrame(upload_file)
    st.write(df)