# streamlit

import streamlit as st 
import requests

st.title("Register..")
server_url="http://127.0.0.1:8000"
with st.form("Register form.."):
    name=st.text_input("Name")
    email=st.text_input("Email")
    password=st.text_input("Password",type="password")
    role=st.selectbox("Choose role :-",["Recruiter","Job_Seeker"])
    btn_register=st.form_submit_button("Register")
    btn_login=st.form_submit_button("Login")

    if btn_login:
        st.switch_page("pages/login.py")

    if btn_register:
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }

        res=requests.post(f'{server_url}/register',json=payload)
        st.write(res)

