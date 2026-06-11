# uvicorn
# fastapi
from fastapi import FastAPI
from database import supabase_c
app=FastAPI()

@app.post("/register")
def register(payload:dict):
    res=supabase_c.table("users").insert(payload).execute()
    return {
        "msg":"user added successfully",
        "res_obj":res
    }

@app.post("/login")
def login(payload:dict):
    e=payload["email"]
    p=payload["password"]
    r=payload["role"]
    res=supabase_c.table("users").select("*").eq("email",e).eq("password",p).eq("role",r).execute()
    
    
    if len(res.data) == 0:
        return{
            "xyz":"no user found with those credentials"
        }
    else:
        return{
        "xyz":res.data
    }    
     
    