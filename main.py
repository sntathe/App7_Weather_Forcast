import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for neext Days")
place = st.text_input("Place:  ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("temperature", "sky"))

st.subheader(f"{option} for the next {days} in {place}")
dates, data = get_data(place, option=option)

dates = dates[0:(days * 8 - 1)]
data = data[0:(days * 8 - 1)]

if option == "temperature":
    if (len(dates) != 0 and len(data) != 0):
        figure = px.line(x=dates, y=data, labels={"x": "Date", "y": "Temprature"})
        st.plotly_chart(figure)

if option == "sky":
    images = {"Clear": "images/clear.png",
              "Clouds": "images/cloud.png",
              "Rain": "images/rain.png",
              "Snow": "images/snow.png"
              }
    sky_conditions = [images[condition] for condition in data]
    st.image(sky_conditions , width = 100)
