from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from app.db.database import get_connection
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm

templates = Jinja2Templates(directory="app/templates")

auth_router = APIRouter()

@auth_router.get("/login", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "pages/login.html", {"request": request}
    )

@auth_router.post("/login", response_class=HTMLResponse)
async def home(request: Request, client = Depends(get_connection), form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.grant_type)
    response = templates.TemplateResponse(
        "pages/login.html", {"request": request}
    )
    response.set_cookie(key="token", value=form_data.password, httponly=True)
    return response