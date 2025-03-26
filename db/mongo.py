import os

from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL_LOCAL")

client = MongoClient(MONGO_URL)

try:
    for db in client.list_databases():
        print(db)
except Exception as e:
    print("Exception: ", e)


def get_collection():
    db = client["comit"]
    collection = db["contexts"]
    return collection
