from sqlmodel import Session, select
from schemas import CreateHero
from models import Hero

def create_hero(session: Session, hero_create: CreateHero):
    hero = Hero.model_validate(hero_create)
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

def get_heros(session: Session, offset: int = 0, limit:int = 100):
    return session.exec(select(Hero).offset(offset).limit(limit)).all()


def get_hero(session: Session, hero_id: int):
    return session.get(Hero, hero_id)