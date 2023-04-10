from fastapi import APIRouter, Request, Depends
from app.db import crud
from app.db.database import get_connection
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
base_router = APIRouter()

@base_router.get("/")
def home(client = Depends(get_connection)):
    print(client.users.find_one({"mail": "lucastofaleti@hotmail.com"}))
    # logged_user = "6433fc97492f3fadfdb98960" #hardcoded, change later
    # tests = crud.get_user_tests()
    # print(tests)
    # if tests:
    #     return "ok"
    # else:
    #     return "none"
    # return tests
    # return templates.TemplateResponse(
    #     "shared/base.html", {"request": request, "user": tests}
    # )