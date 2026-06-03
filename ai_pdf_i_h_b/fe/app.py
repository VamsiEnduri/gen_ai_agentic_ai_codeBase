# fe code with streamlit
import streamlit as st 
import requests

server_loc="http://127.0.0.1:8000"
st.title("AI PDF INTERVIEW HELPER BOT")
c_file=st.file_uploader("choose PDF ",type=["pdf"])

if st.button("Upload PDF"):
    f={
        "file":c_file
    }
    res=requests.post(f"{server_loc}/uploads",files=f)
    st.write(res.json()["msg"])
