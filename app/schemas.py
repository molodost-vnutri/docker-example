from typing import Optional, List
from pydantic import BaseModel
from datetime import date



class Genre(BaseModel):
    name: str

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: Optional[List[Genre]] = None
    pages: int