import fastapi, components.DataBase

app = fastapi.FastAPI()
db = components.DataBase.MSDB()