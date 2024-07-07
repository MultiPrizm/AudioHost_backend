from fastapi import Cookie, responses, Response
from pydantic import BaseModel
from typing import Optional

from AppCore import app, db


class LoginRequest(BaseModel):

    login: str
    password: str


@app.post("/login/reg")
def reg(req: LoginRequest):
    
    res = db.reg_new_user(req.login, req.password)

    if res:
        return responses.HTMLResponse(content=200)
    else:
        return responses.HTMLResponse(status_code=403)
    

@app.post("/login/log")
def log(req: LoginRequest, resp: Response):
    res = db.login_user(req.login, req.password)
    print(req.login)
    if res:
        resp.set_cookie(key="login", value=req.login, httponly=True)

        return responses.JSONResponse(content={})
    else:
        return responses.HTMLResponse(content="403" ,status_code=403)


@app.post("/login/delog")
def gelog():
    
    Response.set_cookie(key="login", value="None")

    return responses.HTMLResponse(content=200)

@app.get("/login/getinfo")
def getinfo(user: Optional[str] = Cookie(None)):
    print(user)
    return responses.JSONResponse(content= {"1": user})