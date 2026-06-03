import streamlit as st
import requests

server_location="http://127.0.0.1:8000"

st.title("Employee Manager System")


menu = st.sidebar.selectbox(
    "Select Option",
    ["Add Employee", "View Employees"]
)

# ADD EMPLOYEE
if menu == "Add Employee":
    st.subheader("Add Employee")

    name = st.text_input("Enter Employee Name")
    age = st.number_input(
        "Enter Employee Age",
        min_value=18,
        max_value=100
    )

    department = st.text_input("Enter Department")
    salary = st.number_input(
        "Enter Salary",
        min_value=10000
    )

    if st.button("Add Employee"):
        emp_data={
            "n":name,
            "a":age,
            "d":department,
            "s":salary
        }

        resobj=requests.post(f"{server_location}/add_employee",json=emp_data)
        st.write(resobj.json())
