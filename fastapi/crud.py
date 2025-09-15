from sqlmodel import Session, select
from schemas import CreateHero, UpdateHero
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

def update_hero(session: Session, hero_id: int, hero_update: UpdateHero):
    hero = session.get(Hero, hero_id)
    if not hero:
        return None
    # update only provide fields
    hero_data = hero_update.model_dump(exclude_unset=True)
    for key, val in hero_data.items():
        setattr(hero, key, val)
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

def delete_hero(session: Session, hero_id: int) -> bool:
    hero = session.get(Hero, hero_id)
    if not hero:
        return False

    session.delete(hero)
    session.commit()
    return True
