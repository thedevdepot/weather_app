import streamlit as st
import plotly.express as px


st.title("The Weather for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forcast days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2022-25-10", "2022-25-11", "2022-25-12"]
temperatures = [10, 11, 15]

figure = px.line(x=dates, y=temperatures, labels={"x": "dates", "y": "temperature (C)"})
st.plotly_chart(figure)