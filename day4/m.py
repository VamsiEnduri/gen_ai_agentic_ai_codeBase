# pip install fastapi
# pip install uvicorn
# pip install mysql-connector-python

from fastapi import FastAPI
import mysql.connector

api = FastAPI()

# MYSQL CONNECTION
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="10000Coders",
    database="apis",
    port=3306
)

cursor = conn.cursor(dictionary=True)

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees2(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100),
    salary INT
)
""")

conn.commit()


# =====================================
# ADD EMPLOYEE
# =====================================
@api.post("/add_employee")
def add_employee(emp_data: dict):

    cursor.execute(
        """
        INSERT INTO employees2(name, age, department, salary)
        VALUES(%s,%s,%s,%s)
        """,
        (
            emp_data["name"],
            emp_data["age"],
            emp_data["department"],
            emp_data["salary"]
        )
    )

    conn.commit()

    return {
        "message": "Employee Added Successfully"
    }


# =====================================
# GET ALL EMPLOYEES
# =====================================
@api.get("/get_employees")
def get_employees():

    cursor.execute(
        "SELECT * FROM employees2"
    )

    data = cursor.fetchall()

    return data


# =====================================
# GET SINGLE EMPLOYEE
# =====================================
@api.get("/get_single_employee/{id}")
def get_single_employee(id: int):

    cursor.execute(
        "SELECT * FROM employees2 WHERE id=%s",
        (id,)
    )

    data = cursor.fetchone()

    return data


# =====================================
# UPDATE EMPLOYEE
# =====================================
@api.put("/update_employee/{id}")
def update_employee(id: int, emp_data: dict):

    cursor.execute(
        """
        UPDATE employees2
        SET name=%s,
            age=%s,
            department=%s,
            salary=%s
        WHERE id=%s
        """,
        (
            emp_data["name"],
            emp_data["age"],
            emp_data["department"],
            emp_data["salary"],
            id
        )
    )

    conn.commit()

    return {
        "message": "Employee Updated Successfully"
    }


# =====================================
# DELETE EMPLOYEE
# =====================================
@api.delete("/delete_employee/{id}")
def delete_employee(id: int):

    cursor.execute(
        "DELETE FROM employees2 WHERE id=%s",
        (id,)
    )

    conn.commit()

    return {
        "message": "Employee Deleted Successfully"
    }