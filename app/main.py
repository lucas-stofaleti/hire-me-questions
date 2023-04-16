from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from app.routes import *
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.exception_handler(RequestValidationError)
async def not_found_exception_handler(request: Request, exc: RequestValidationError):
    print(request.url.path)
    return RedirectResponse(f'{request.base_url}{request.url.path[1:]}?error={exc}', status_code=303)

app.include_router(base_router)
app.include_router(auth_router)