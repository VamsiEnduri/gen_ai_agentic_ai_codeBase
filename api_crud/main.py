# uvicorn :-- server name 
# FastAPI() :-- api creator in backend
# pip install uvicorn fastapi

from fastapi import FastAPI  
import mysql.connector

conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    database="api_crud",
    password="10000Coders"
)

cursor_obj=conn_obj.cursor(dictionary=True)


app=FastAPI() # object of FastAPI

@app.post("/add_emp") # backend api post data :-- args new_data json
def add_employee__(new_data : dict):# type annotation
    name = new_data["n"]
    email = new_data["e"]
    department = new_data["d"]

    query="insert into emps(name,email,department) values(%s,%s,%s)"
    values=(name,email,department)

    cursor_obj.execute(query,values)

    conn_obj.commit()

    return {
        "msg":f"{name} user added successfully"
    }

@app.get("/get_emps")
def get_emps__():
    query="select * from emps"
    cursor_obj.execute(query)
    data=cursor_obj.fetchall()

    return {
        "all_emps":data
    }

@app.delete("/delete_emp/{emp_id}")
def delete_emp__(emp_id:int):
    query="delete from emps where id = %s"
    values=(emp_id,)

    cursor_obj.execute(query,values)
    conn_obj.commit()

    return {
        "msg_delete":f"the employee with {emp_id} is deleted successfully.."
    }
# type erroe :-- forward_ref :
# pip install --upgrade uvicorn 

@app.get("/get_single_employee/{emp_id}")
def get_single_emp__(emp_id:int):
    query="select * from emps where id = %s"
    values=(emp_id,)

    cursor_obj.execute(query,values)
    emp_data=cursor_obj.fetchone()
    return {
        "emp_data":emp_data
    }
# uvicorn filename:objectname --reload


@app.put("/update_employee/{emp_id}")
def update_employee__(emp_id:int,updated_emp_data:dict):
    query="update emps set name=%s,email=%s,department=%s where id = %s"
    values=(updated_emp_data["n"],updated_emp_data['e'],updated_emp_data["d"],emp_id)
    cursor_obj.execute(query,values)
    conn_obj.commit()

    return{
        "updated_msg":f"{emp_id} emp updated"
    }
