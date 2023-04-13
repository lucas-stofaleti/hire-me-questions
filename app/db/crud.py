from app.db.database import get_connection, client
from fastapi import Depends
from bson.objectid import ObjectId
import pymongo

def get_user_tests(db = Depends(get_connection)):
    print(db.users.find({"mail": "lucastofaleti@hotmail.com"}))