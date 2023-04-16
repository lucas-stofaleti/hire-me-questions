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

def test_signup_get():
    response = client.get("/signup")
    assert response.status_code == 200

def test_signup_post_without_inputs():
    response = client.post("/signup")
    print(response.json())
    print(response.content)
    assert response.status_code == 200