import streamlit as st
import requests

S_URL = "http://127.0.0.1:8000"

st.title("🌤 AI Weather Agent")

city = st.text_input(
    "Enter City"
)

question = st.text_input(
    "Ask Your Weather Question"
)


if st.button("Ask Agent"):
    res=requests.post(f"{S_URL}/get_weather",params={
        "city":city,
        "question":question
    })

    st.success(res.json()["messages"][-1]["content"])
