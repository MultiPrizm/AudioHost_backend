import fastapi, pydantic, components.logger, components.StreamAudio, components.DownloadAudio, components.InfoCenter, components.Login

from AppCore import app

class UserRequest(pydantic.BaseModel):

    login: str
    name: str
    lastname: str
    age: int

@app.get("/")
async def index():

    return fastapi.responses.RedirectResponse("/")
