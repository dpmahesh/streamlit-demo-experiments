import numpy as np
import pandas as pd
import streamlit as st


st.title("Welcome to the  Demo App")

st.sidebar.header("User Input Parameters")
x=st.sidebar.slider("User Input Data")
y=st.sidebar.date_input("When is your birthday")
z=st.sidebar.text_input('Enter First Name:')

st.write("The dat you entered by moving the slider on the left:")
st.header(x)

st.write("Your Date of Birth")
st.header(y)
st.write("The text you enetered in the input field in the side bar")
st.header(z)

chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)
st.line_chart(chart_data)
