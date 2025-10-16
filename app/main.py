from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.api.endpoints import users

app = FastAPI(title="FastAPI + Postgres (local app)")

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["Users"])
