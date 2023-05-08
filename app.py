import numpy as np
import pandas as pd
import streamlit as st


st.title("Welcome to the  Demo App")

st.sidebar.header("User Input Parameters")
x=st.sidebar.slider("User Input Data")
y=st.sidebar.date_input("When is your birthday")
z=st.sidebar.text_input('Enter First Name:')

st.header("Move the slider in the sidebar to update below:")
st.subheader(x)

st.header("Enter your Date of Birth in the sidebar")
st.subheader(y)

st.header("The text from the input field in the side bar")
st.subheader(z)


chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.header("Some sample charts")
st.bar_chart(chart_data)
st.line_chart(chart_data)
