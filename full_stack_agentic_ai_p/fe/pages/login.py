import streamlit as st 
import requests
from streamlit_local_storage import LocalStorage

ls=LocalStorage()

st.title("Login....")
server_url="http://127.0.0.1:8000"

with st.form("Login form.."):
    email=st.text_input("Email")
    password=st.text_input("Password",type="password")
    role=st.selectbox("Choose role :-",["Recruiter","Job_Seeker"])
    btn_login=st.form_submit_button("Login")

    if btn_login:
        payload = {
            "email": email,
            "password": password,
            "role": role
        }
        # pip install streamlit-local-storage
        res=requests.post(f'{server_url}/login',json=payload)
        data=res.json()["xyz"]
        if isinstance(data,list):
            ls.setItem("logged_User",data[0])
            l_user=ls.getItem("logged_User")
            l_email=l_user["email"]
            l_role=l_user["role"]

            if l_role == "Recruiter":
                st.switch_page("pages/R_Dashboard.py")
            elif l_role=="Job_Seeker":
                st.switch_page("pages/J_Dashboard.py")

        if isinstance(data,str):
            st.write(data)


        # res.json()["xyz"][0]
        # ls.setItem("loggedIn_user",res.json()["xyz"])
        # st.write(res.json()["xyz"])