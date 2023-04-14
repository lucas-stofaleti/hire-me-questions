from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from app.db.database import get_connection
from fastapi.templating import Jinja2Templates
from app.utils.form import get_form

templates = Jinja2Templates(directory="app/templates")

auth_router = APIRouter()

@auth_router.get("/login", response_class=HTMLResponse)
def home(request: Request, client = Depends(get_connection)):
    return templates.TemplateResponse(
        "pages/login.html", {"request": request}
    )

@auth_router.post("/login", response_class=HTMLResponse)
async def home(request: Request, client = Depends(get_connection), form = Depends(get_form)):
    print(form)
    return templates.TemplateResponse(
        "pages/login.html", {"request": request}
    )