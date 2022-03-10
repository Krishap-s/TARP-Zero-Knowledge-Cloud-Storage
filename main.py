from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return "OK"
