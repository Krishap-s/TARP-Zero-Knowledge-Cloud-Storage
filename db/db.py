import os
from pymongo import MongoClient
import pymongo

client = None

def get_database():
    global client
    if client != None:
        return client
    client = MongoClient(os.environ.get("DATABASE_URL"))
    db = client.encrypt_everywhere
    return db