from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_table

from routers import hero
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    #load on start up
    create_db_and_table()
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hero.router)

