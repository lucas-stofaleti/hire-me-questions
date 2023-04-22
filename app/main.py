from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from app.routes import *
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(base_router)
app.include_router(auth_router)