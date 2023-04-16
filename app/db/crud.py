from app.db.database import get_connection
import pymongo
import mongomock
from fastapi import Depends
from app.models.forms import *

def get_user_tests(db = Depends(get_connection)):
    print(db.users.find({"mail": "lucastofaleti@hotmail.com"}))

def get_user(db, mail: str):
    return db.users.find_one({"mail": mail})

def register_user(db, form_data: RegistrationForm, permissions: list = [], is_active: bool = True):
    user = {
        "name": form_data.name,
        "surname": form_data.surname,
        "mail": form_data.mail,
        "hashed_password": form_data.password,
        "is_active": is_active,
        "permissions": permissions
    }
    user = db.users.insert_one(user)
    return user.inserted_id
    