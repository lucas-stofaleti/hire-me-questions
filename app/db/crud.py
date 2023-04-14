from app.db.database import get_connection
from fastapi import Depends

def get_user_tests(db = Depends(get_connection)):
    print(db.users.find({"mail": "lucastofaleti@hotmail.com"}))