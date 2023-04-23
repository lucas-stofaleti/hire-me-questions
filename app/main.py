from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from app.routes import *
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(base_router)
app.include_router(auth_router)

@app.exception_handler(401)
async def unicorn_exception_handler(request: Request, exc):
    html_content = """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=529)