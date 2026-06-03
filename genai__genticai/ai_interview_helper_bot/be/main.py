from fastapi import FastAPI,Request
from openai import OpenAI # import 2
# pip install openai  1

app =FastAPI()


@app.get("/")
def home():
    return {
        "msg":"you are on HOME"
    }
# client creation 3 client object 
# create chestunnaru OpenAI() 
#CLIENT OBJECT

@app.post("/generate")
async def prompt_rec_function(req :Request):
    data=await req.json()
    print(data)
    p=data["prompt"]

    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
           { "role":"user",
            "content":p}
        ]
    )

    answer = response.choices[0].message.content
    return { "object": answer }


    