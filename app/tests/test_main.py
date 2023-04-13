from fastapi.testclient import TestClient
import mongomock
from app.main import app
from app.db.database import get_connection

mongo = mongomock.MongoClient()
db = mongo.get_database("hireme")
col = db.get_collection('users')
col.insert_one({'mail': 'lucastofaleti@hotmail.com'})
client = TestClient(app)

def connection_override():
    return db

app.dependency_overrides[get_connection] = connection_override

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "lucastofaleti@hotmail.com"
