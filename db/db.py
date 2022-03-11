import os
from pymongo import MongoClient,database
import pymongo

db:database.Database = None

def get_database() -> database.Database:
    global db
    if db != None:
        return db
    client = MongoClient(os.environ.get("DATABASE_URL"))
    db = client[os.environ["DATABASE_NAME"]]
    return db