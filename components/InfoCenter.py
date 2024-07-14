import fastapi

from AppCore import app, db

@app.get("/info/list")
def get_audio_list():

    audiolist = db.get_popular_audio()
    
    res = {
        "response": audiolist
    }

    return fastapi.responses.JSONResponse(res)