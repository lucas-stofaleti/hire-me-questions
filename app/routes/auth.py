from fastapi import APIRouter, Request, Depends, Cookie, status
from fastapi.responses import HTMLResponse
from app.db.database import get_connection
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.auth import *
from app.models.forms import RegistrationForm
from app.db.crud import *
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="app/templates")

auth_router = APIRouter()

@auth_router.get("/login", response_class=HTMLResponse)
def login(request: Request, error: str | None = None, msg: str | None = None):
    return templates.TemplateResponse(
        "pages/login.html", {"request": request, "msg": msg}
    )

@auth_router.post("/login", response_class=HTMLResponse)
def login_post(request: Request, client = Depends(get_connection), form_data: OAuth2PasswordRequestForm = Depends()):
    print(f"Normal Password: {form_data.password}")
    print(f"Hashed Password: {get_password_hash(form_data.password)}")
    print(verify_password(form_data.password, get_password_hash(form_data.password)))
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username, "role": ["test:write", "test:read"]}, expires_delta=access_token_expires
    )
    response = templates.TemplateResponse(
        "pages/login.html", {"request": request}
    )
    response.set_cookie(key="token", value=access_token, httponly=True)
    return response

@auth_router.get("/signup", response_class=HTMLResponse)
def signup(request: Request, error: str | None = None):
    return templates.TemplateResponse(
        "pages/register.html", {"request": request, "error": error}
    )

@auth_router.post("/signup", response_class=HTMLResponse)
def signup_post(client = Depends(get_connection), form_data: RegistrationForm = Depends(RegistrationForm.as_form)):
    user = get_user(db=client, mail=form_data.mail)
    if user:
        return RedirectResponse("/signup?error=User already registered!", status_code=status.HTTP_303_SEE_OTHER)
    form_data.password = get_password_hash(form_data.password)
    user_id = register_user(db=client, form_data=form_data)
    return RedirectResponse("/login?msg=User created! Please Login.", status_code=status.HTTP_303_SEE_OTHER)