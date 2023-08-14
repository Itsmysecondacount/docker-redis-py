from fastapi import FastAPI, HTTPException

import requests

from telegram import Bot

from model import Timbre

from datetime import datetime

from database import fetch_all_todos, create_todo

# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware

TOKEN = "6072798764:AAEHhNTNdmkN6-3eA1lvBInfSo8rRisEDu4"
CHAT_ID = "5419402277"


async def enviar_mensaje(mensaje):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=mensaje)

    return "correcto"


app = FastAPI()

origins = ["http://localhost:3000", "*"]

# what is a middleware?
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/api/timbre")
async def get_timbre():
    response = fetch_all_todos()
    return response


@app.post("/api/timbre/", response_model=Timbre)
async def post_timbre(timbre: Timbre):
    data = timbre.dict()
    data["datetime"] = datetime.now()
    response = create_todo(data)
    if response:
        mensaje = await enviar_mensaje(data["message"])
        response_2 = requests.get("http://192.168.0.31/toggle")
        # Aquí mando una solicitud http al arduino de mi cuarto
        return response
    raise HTTPException(400, "Something went wrong")
