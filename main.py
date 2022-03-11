from fastapi import FastAPI
from api.user import UserRouter
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Encrypt Everywhere")


@app.get("/healthcheck")
async def healthcheck():
    return "OK"

app.include_router(UserRouter)