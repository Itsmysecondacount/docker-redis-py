#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

# Pydantic allows auto creation of JSON Schemas from models
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Timbre(BaseModel):
    message: str
    datetime: Optional[datetime]