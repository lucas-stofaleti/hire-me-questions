from fastapi.encoders import jsonable_encoder
from fastapi import Request

async def get_form(request: Request):
    form = await request.form()
    return jsonable_encoder(form)