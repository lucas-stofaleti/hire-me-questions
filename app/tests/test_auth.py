from fastapi.testclient import TestClient
import mongomock
from app.main import app
from app.db.database import get_connection
from app.utils.auth import *

mongo = mongomock.MongoClient()
db = mongo.get_database("hireme")
col = db.get_collection('users')
col.insert_one({'mail': 'lucastofaleti@hotmail.com'})
client = TestClient(app)

def connection_override():
    return db

app.dependency_overrides[get_connection] = connection_override

# Utils
def test_password_hash():
    password = "mypassword"
    hashed_password = get_password_hash(password)
    check_passwords = verify_password(password, hashed_password)
    assert check_passwords == True

# Endpoints
def test_signup_get():
    response = client.get("/signup")
    assert response.status_code == 200

def test_signup_post_without_inputs():
    response = client.post("/signup")
    assert response.status_code == 422