from pydantic import BaseModel
from fastapi import Form

class LoginForm(BaseModel):
    mail: str
    password: str

    @classmethod
    def as_form(
        cls,
        mail: str = Form(...),
        password: str = Form(...)
    ):
        return cls(mail=mail, password=password)