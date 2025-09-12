from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_table

from routers import hero


@asynccontextmanager
async def lifespan(app: FastAPI):
    #load on start up
    create_db_and_table()
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)
app.include_router(hero.router)

