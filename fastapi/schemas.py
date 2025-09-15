from sqlmodel import SQLModel
from typing import Optional

class CreateHero(SQLModel):
    name: str
    age: Optional[int] = None
    secret_name: str

class ReadHero(SQLModel):
    id: int
    name: str
    age: Optional[int] = None
    secret_name: str

class UpdateHero(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None
    secret_name: Optional[str] = None