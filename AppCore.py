import fastapi, components.DataBase, components.AppCryptographer, components.S3, colorama, json

config = None

with open("conf.json", 'r') as conf:
    config = conf.read()
    config = json.loads(config)

colorama.init()

app = fastapi.FastAPI()
db = components.DataBase.MSDB()
ac = components.AppCryptographer.AppCryptographer()
s3 = components.S3.S3(not config["awscli"])