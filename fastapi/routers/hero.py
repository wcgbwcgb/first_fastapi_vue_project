from fastapi import APIRouter, Depends, Query, HTTPException, status
from schemas import CreateHero, ReadHero
from typing import Annotated
from database import get_session
from sqlmodel import Session

import crud

router = APIRouter(prefix="/heros", tags=["hero"])
SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/", response_model=CreateHero)
def create(hero: CreateHero, session:SessionDep):
    return crud.create_hero(session, hero)

@router.get("/", response_model=list[ReadHero])
def read_all(session:SessionDep, offset:int = 0, limit: Annotated[int, Query(le=100)] = 100):
    return crud.get_heros(session, offset, limit)

@router.get("/{hero_id}", response_model=ReadHero)
def read(session:SessionDep, hero_id:int):
    hero =  crud.get_hero(session, hero_id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no hero with this id")
    return hero