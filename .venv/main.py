import streamlit as st
import plotly.express as px
from backend import get_data

st.title("The Weather for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forcast days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=d, y=t, labels={"x": "Date" y: "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/clouds.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["Weather"][0]["Main"] for dict in filtered_data]
        print(sky_conditions)
        st.image(image_paths, width=115)

except KeyError:
    st.write("Try another city.")