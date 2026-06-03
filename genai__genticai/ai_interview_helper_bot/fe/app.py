import streamlit as st
import requests
import ast
be_url ="http://127.0.0.1:8000"
st.title("AI Interview Preparation Helper Bot")

with st.form("Details "):
    Topic=st.text_input("Enter Lang-Topic :--")
    level=st.selectbox("choose level ",["Easy","Medium","Advanced"])
    ways=st.multiselect("choose any of below ",["MCQS","Theory Questions","Coding questions"])
    st.write(ways)

    if st.form_submit_button():

        
        prompt = f"""

        Generate only interview questions.

        Topic: {Topic}

        Level: {level}

        Question Types:
        {",".join(ways)}

        IMPORTANT RULES:

        1. Return ONLY python list of dictionaries
        2. Do NOT return explanations
        3. Do NOT return introductions
        4. Do NOT return markdown
        5. Do NOT return headings
        6. Do NOT return text outside list
        7. Each dictionary must contain:
        - question - type


    Generate 10 questions.

"""

        response=requests.post(f"{be_url}/generate",json={"prompt":prompt})
        st.write(response.status_code)

        if response.status_code == 200:
            res=response.json()
            qns=ast.literal_eval(res["object"])
            for q in qns:
                st.write(q["question"])
            # list(res["object"])
            # data=ast.literal_eval(res["object"])
            # for q in data:
            #     st.write(q["question"])



