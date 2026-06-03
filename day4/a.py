# pip install streamlit
# pip install requests
# pip install pandas

import streamlit as st
import requests
import pandas as pd

server_location = "http://127.0.0.1:8000"

st.title("Employee Manager System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Add Employee",
        "View Employees",
        "Update Employee",
        "Delete Employee"
    ]
)

# =====================================
# ADD EMPLOYEE
# =====================================
if menu == "Add Employee":

    st.subheader("Add Employee")

    name = st.text_input("Enter Employee Name")

    age = st.number_input(
        "Enter Employee Age",
        min_value=18,
        max_value=100
    )

    department = st.text_input(
        "Enter Department"
    )

    salary = st.number_input(
        "Enter Salary",
        min_value=10000
    )

    if st.button("Add Employee"):

        emp_data = {
            "name": name,
            "age": age,
            "department": department,
            "salary": salary
        }

        response = requests.post(
            f"{server_location}/add_employee",
            json=emp_data
        )

        st.success(response.json()["message"])


# =====================================
# VIEW EMPLOYEES
# =====================================
elif menu == "View Employees":

    st.subheader("All Employees")

    response = requests.get(
        f"{server_location}/get_employees"
    )

    data = response.json()

    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.warning("No Employees Found")


# =====================================
# UPDATE EMPLOYEE
# =====================================
elif menu == "Update Employee":

    st.subheader("Update Employee")

    emp_id = st.number_input(
        "Enter Employee ID",
        min_value=1,
        step=1
    )

    # LOAD OLD DATA
    if st.button("Load Employee Data"):

        response = requests.get(
            f"{server_location}/get_single_employee/{emp_id}"
        )

        old_data = response.json()

        if old_data:
            st.session_state.old_data = old_data
        else:
            st.error("Employee Not Found")

    # SHOW OLD DATA IN FORM
    if "old_data" in st.session_state:

        old = st.session_state.old_data

        name = st.text_input(
            "Enter Name",
            value=old["name"]
        )

        age = st.number_input(
            "Enter Age",
            min_value=18,
            max_value=100,
            value=old["age"]
        )

        department = st.text_input(
            "Enter Department",
            value=old["department"]
        )

        salary = st.number_input(
            "Enter Salary",
            min_value=10000,
            value=old["salary"]
        )

        if st.button("Update Employee"):

            updated_data = {
                "name": name,
                "age": age,
                "department": department,
                "salary": salary
            }

            response = requests.put(
                f"{server_location}/update_employee/{emp_id}",
                json=updated_data
            )

            st.success(response.json()["message"])


# =====================================
# DELETE EMPLOYEE
# =====================================
elif menu == "Delete Employee":

    st.subheader("Delete Employee")

    emp_id = st.number_input(
        "Enter Employee ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Employee"):

        response = requests.delete(
            f"{server_location}/delete_employee/{emp_id}"
        )

        st.success(response.json()["message"])