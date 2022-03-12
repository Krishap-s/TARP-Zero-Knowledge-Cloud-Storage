from fastapi import FastAPI
from api.user import UserRouter
import os

app = FastAPI(title="Encrypt Everywhere")


@app.get("/healthcheck")
async def healthcheck():
    return "OK"

app.include_router(UserRouter)