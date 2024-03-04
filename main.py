from fastapi import FastAPI
from pydantic import BaseModel

class dataModel(BaseModel):
    name : str
    phone : int

app =FastAPI()

@app.get("/")
def hel():
    return 'Start FastAPI by Gtend'


@app.post("/send")
def postData(data:dataModel):
    print(data)
    return "전송완료"