import pymongo

db = client.hireme

async def get_connection():
    print(f"Client: {client}")
    
    return db
