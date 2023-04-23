class User:
  def __init__(self, payload: dict):
    self.id = payload["_id"]
    self.name = payload["name"]
    self.surname = payload["surname"]
    self.mail = payload["mail"]
    self.is_admin = payload["is_admin"]