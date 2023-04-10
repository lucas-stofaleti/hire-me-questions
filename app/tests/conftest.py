import pytest
import mongomock

# @pytest.fixture()
# def mongo_mock(monkeypatch):
#     client = mongomock.MongoClient()
#     db = client.get_database("hireme")

#     def fake_db():
#         return db

#     monkeypatch.setattr("app.db.crud.get_connection", fake_db)

@pytest.fixture()
def mongo_mock(monkeypatch):
    client = mongomock.MongoClient()
    db = client.get_database("hireme")

    def fake_db():
        return db

    monkeypatch.setattr("app.db.database.client", fake_db)