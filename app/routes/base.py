from fastapi import APIRouter, Request, Depends, Cookie, HTTPException
from app.db import crud
from fastapi.responses import HTMLResponse
from app.db.database import get_connection
from fastapi.templating import Jinja2Templates
from app.utils.auth import auth_cookie
from app.models.user import User

templates = Jinja2Templates(directory="app/templates")

base_router = APIRouter()

@base_router.get("/", response_class=HTMLResponse)
def home(request: Request, client = Depends(get_connection), user: User = Depends(auth_cookie)):
    response = templates.TemplateResponse(
        "shared/base.html", {"request": request}
    )
    return response