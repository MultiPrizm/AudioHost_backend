import fastapi

from AppCore import app, db

@app.get("/info/list/{page}")
async def get_audio_list(page: int):

    audiolist = db.get_popular_audio(page)
    
    res = {
        "response": audiolist
    }

    return fastapi.responses.JSONResponse(res)