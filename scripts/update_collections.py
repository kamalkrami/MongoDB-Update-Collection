from db.mongo import get_collection


def update_collections():
    collections = get_collection()
    documents = collections.find()
    for doc in documents:
        _id = str(doc["_id"])
        userid = _id.split("_")[0]
        collections.update_one({"_id": doc["_id"]}, {"$set": {"userId": userid}})


if __name__ == "__main__":
    update_collections()
