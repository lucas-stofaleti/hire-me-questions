from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from app.db.database import get_connection
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

auth_router = APIRouter()

@auth_router.get("/login", response_class=HTMLResponse)
def home(request: Request, client = Depends(get_connection)):
    return templates.TemplateResponse(
        "pages/login.html", {"request": request}
    )