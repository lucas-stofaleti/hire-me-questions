from fastapi import APIRouter, Request, Depends, status
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
        "pages/login.html", {"request": request, "msg": msg, "error": error}
    )

@auth_router.post("/login", response_class=HTMLResponse)
def login_post(request: Request, client = Depends(get_connection), form_data: OAuth2PasswordRequestForm = Depends()):
    error = "Wrong mail or password!"
    user = get_user(db=client, mail=form_data.username)
    if not user:
        return RedirectResponse(f"/login?error={error}", status_code=status.HTTP_303_SEE_OTHER)
    elif not user["is_active"]:
        return RedirectResponse("/login?error=User is not activated!", status_code=status.HTTP_303_SEE_OTHER)
    elif not verify_password(form_data.password, user["hashed_password"]):
        return RedirectResponse(f"/login?error={error}", status_code=status.HTTP_303_SEE_OTHER)
    user["_id"] = str(user["_id"])
    del user["hashed_password"]
    del user["is_active"]
    access_token = create_access_token(
        data=user
    )
    response = RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="token", value=access_token, httponly=True, expires=settings.access_token_expire_minutes*60)
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