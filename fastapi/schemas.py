from sqlmodel import SQLModel
from typing import Optional

class CreateHero(SQLModel):
    name: str
    age: Optional[int] = None
    secret_name: str

class ReadHero(SQLModel):
    name: str
    age: Optional[int] = None
    secret_name: str