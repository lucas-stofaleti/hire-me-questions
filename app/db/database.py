import pymongo
from app.utils.settings import settings

client = pymongo.MongoClient(f"mongodb+srv://{settings.mongo_user}:{settings.mongo_password}@{settings.mongo_url}/?retryWrites=true&w=majority")
db = client.hireme

def get_connection():
    return db
