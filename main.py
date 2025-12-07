from fastapi import FastAPI
from pydantic import BaseModel
from vtop_scraper import VTOPSession

app = FastAPI()
vtop = VTOPSession()

class LoginData(BaseModel):
    username: str
    password: str
    captcha: str

@app.post("/login")
def login(data: LoginData):
    success = vtop.login(data.username, data.password, data.captcha)
    return {"success": success}

@app.get("/attendance")
def attendance():
    return vtop.get_attendance()

@app.get("/marks")
def marks():
    return vtop.get_marks()

@app.get("/timetable")
def timetable():
    return vtop.get_timetable()
