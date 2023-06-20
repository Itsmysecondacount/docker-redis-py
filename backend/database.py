#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio
from model import Timbre

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.timbre
collection = database.timbrada

async def recuperar_timbres():
    timbres = []
    cursor = collection.find({})
    async for document in cursor:
        timbres.append(Timbre(**document))
    return timbres

async def timbrada(todo):
    document = todo
    result = await collection.insert_one(document)
    return document