from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import *
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(base_router)
app.include_router(auth_router)