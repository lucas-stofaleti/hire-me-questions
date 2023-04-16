from pydantic import BaseModel
from fastapi import Form

class RegistrationForm(BaseModel):
    name: str
    surname: str
    mail: str
    password: str

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        surname: str = Form(...),
        mail: str = Form(...),
        password: str = Form(...)
    ):
        return cls(name=name, surname=surname, mail=mail, password=password)