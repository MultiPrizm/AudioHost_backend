from fastapi import Cookie, responses, Request
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
        return responses.JSONResponse(content={"success": True}, status_code=200)
    else:
        return responses.JSONResponse(content={"success": False})
    

@app.post("/login/log", response_model=dict)
def log(req: LoginRequest):
    res = db.login_user(req.login, req.password)
    if res:
        resp = responses.JSONResponse(content={"success": True}, status_code=200)
        resp.set_cookie("login", req.login, httponly=True)

        return resp
    else:
        return responses.JSONResponse(content={"success": False}, status_code=403)


@app.post("/login/delog")
def gelog():
    
    res = responses.JSONResponse(content={"success": True})
    res.set_cookie("login", "None", httponly=True, secure=True)

    return res

@app.get("/login/getinfo")
def getinfo(user: Request):
    return responses.JSONResponse(content= {"login": user.cookies.get("login")})

@app.get("/cookie")
def check_cookie(req: Request):
    
    if not "Cookie" in req.headers:
        res = responses.JSONResponse(content={})
        res.headers["Set-Cookie"] = "same-site=strict"

        return res
    
    else:

        return responses.JSONResponse(content={})