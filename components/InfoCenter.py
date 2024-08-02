import fastapi

from AppCore import app, db

@app.get("/info/list/{page}")
async def get_audio_list(page: int):

    audiolist = db.get_popular_audio(page)
    
    res = {
        "response": audiolist
    }

    return fastapi.responses.JSONResponse(res)

@app.get("/info/playlist")
async def get_audio_list(user: fastapi.Request):

    audiolist = db.get_playlist(user.cookies.get("login"))

    audiolist = db.get_tracks_from_id(audiolist)
    
    res = {
        "response": audiolist
    }

    return fastapi.responses.JSONResponse(res)

@app.post("/info/playlist/add/{id}")
async def get_audio_list(user: fastapi.Request, id: str):

    audiolist = db.get_playlist(user.cookies.get("login"))

    if not id in audiolist:
        audiolist.append(id)

    dbres = db.update_playlist(audiolist, user.cookies.get("login"))
    
    res = {
        "success": dbres
    }

    return fastapi.responses.JSONResponse(res)

@app.post("/info/playlist/del/{id}")
async def get_audio_list(user: fastapi.Request, id: str):

    audiolist = db.get_playlist(user.cookies.get("login"))

    if id in audiolist:
        audiolist.remove(id)
    print(audiolist)
    dbres = db.update_playlist(audiolist, user.cookies.get("login"))
    
    res = {
        "success": dbres
    }

    return fastapi.responses.JSONResponse(res)