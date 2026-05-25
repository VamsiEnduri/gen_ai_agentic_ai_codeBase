# pip install fastapi 
# pip install uvicorn 
from fastapi import FastAPI

api=FastAPI()

import mysql.connector


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

@api.post("/add_employee")
def add_e(emp_data:dict):
    cursor.execute(
        """
        INSERT INTO employees2(name, age, department, salary)
        VALUES(%s,%s,%s,%s)
        """,
        (
            emp_data["n"],
            emp_data["a"],
            emp_data["d"],
            emp_data["s"]
        )
    )

    conn.commit()

    return {
        "message":"Employee Added Successfully"
    }
