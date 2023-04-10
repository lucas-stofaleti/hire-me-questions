from fastapi.testclient import TestClient
import mongomock
from app.main import app
from app.db.crud import get_user_tests
import pymongo
client = TestClient(app)


def test_read_main(mongo_mock):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() != "ok"


# def test_get_user_tests(mongo_mock):
#     response = []
#     response = get_user_tests("6433fc97492f3fadfdb98960")
#     # print(response)
#     assert response == []

def test_get_user_tests(mongo_mock):
    response = []
    response = get_user_tests("6433fc97492f3fadfdb98960")
    # print(response)
    assert response == []

# @mongomock.patch(servers=(('server.example.com', 27017),))
# def test_get_user_tests():
#     db = pymongo.MongoClient('server.example.com')
#     db = db.get_database("hireme")
#     response = []
#     response = get_user_tests("6433fc97492f3fadfdb98960")
#     # print(response)
#     assert response == []
    
