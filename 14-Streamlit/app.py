import streamlit as st
import numpy as np 
import pandas as pd 

st.title("Hello, using streamlit")

st.write("A simple textt")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

## Display the Dataframe
st.write("Here is the dataframe")
st.write(df)

##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,4),columns=['a','b','c','d']
)
st.line_chart(chart_data)