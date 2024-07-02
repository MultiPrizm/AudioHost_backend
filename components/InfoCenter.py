import fastapi

from AppCore import app

test = ["test.mp3", "qqq"]

@app.get("/info/list")
def get_audio_list():
    
    res = {
        "response": test
    }

    return fastapi.responses.JSONResponse(res)