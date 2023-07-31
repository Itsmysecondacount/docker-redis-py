from fastapi import FastAPI, HTTPException

from model import Timbre

from datetime import datetime

from database import (
    fetch_all_todos,
    create_todo
)

# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",
    "*"
]

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
        #Aquí me comunico con telegram
        #Aquí mando una solicitud http al arduino de mi cuarto
        return response
    raise HTTPException(400, "Something went wrong")
