import streamlit as st
import requests
import pandas as pd
server_loc = "http://127.0.0.1:8000"

# python -m streamlit run app.py
# python -m uvicorn main:app --reload 

st.title("CRUD operations using the API")

opt=st.sidebar.selectbox("choose operation:-- ",["add_employee","view_employees","update_employee","delete_employee"])

if opt == "add_employee":
    st.header("Adding Employee")
    with st.form("adding"):
        name = st.text_input("Name")
        email=st.text_input("Email")
        dept =st.selectbox("department :-- ",["","dev","tester","aws","devops","ai/ml engineer","gen_ai/agentic_ai devloper"])
        btn=st.form_submit_button("AddEmployee")

    if btn:
        new_data={
            "n":name,
            "e":email,
            "d":dept
        }
        res=requests.post(f"{server_loc}/add_emp",json=new_data) #api post (1,2) # 2 args 
        # 1 :-- url 2 :- data to be sent but as json

        st.write(res.json()) # incoming json formatted response :-- py dict

elif opt== "view_employees":
    if st.button("GetEmps"):
        res=requests.get(f"{server_loc}/get_emps") #fe api
        all_emp_data=res.json() #res storing
        abc=all_emp_data["all_emps"]
        pd_df=pd.DataFrame(abc)
        st.dataframe(pd_df) # table kinda displaying
        
elif opt== "update_employee":
    st.header("Update Employee")
    emp_id = st.number_input("Emp_id",min_value=1,step=1)
    if st.button("FetchEmpData"):
        res=requests.get(f"{server_loc}/get_single_employee/{emp_id}")
        st.write(res.json())
        if res.status_code == 200:
            # emp_data____=res.json()["emp_data"]
            st.session_state.name = res.json()["emp_data"]["name"]
            st.session_state.email = res.json()["emp_data"]["email"]
            st.session_state.department = res.json()["emp_data"]["department"]



    name = st.text_input("name",value=st.session_state.name)
    email = st.text_input("email",value=st.session_state.email)
    department = st.text_input("department",value=st.session_state.department)
    if st.button("UpdateEmployeee"):
        updated_emp_data={
                    "n":name,
                    "e":email,
                    "d":department
                }
        res=requests.put(f"{server_loc}/update_employee/{emp_id}",json=updated_emp_data)

        if res.status_code==200:
            st.success(res.json()["updated_msg"])


elif opt== "delete_employee":
    st.header("Deleting Employee") 

    res=requests.get(f"{server_loc}/get_emps") #fe api
    all_emp_data=res.json() #res storing
    abc=all_emp_data["all_emps"]
    pd_df=pd.DataFrame(abc)
    st.dataframe(pd_df) # table kinda displaying

    emp_id_to_delete=st.number_input("Id ToDelete")
    # print(type(emp_id_to_delete))

    if st.button("Delete"):
        res=requests.delete(f"{server_loc}/delete_emp/{emp_id_to_delete}") 
        if res.status_code == 200:
            st.info(res.json()["msg_delete"])
