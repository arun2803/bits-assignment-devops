from pymongo import MongoClient


def mongodb_connect():
    try:
        client = MongoClient('mongodb://stack:0F1fr@1.1.1.1/default_db?authSource=st2')
        return client
# Removed Exception handling from this function

def get_username_from_mongodb(token_id):
    try:
        client = mongodb_connect()
        db = client['st2']
        token_d_b = db.token_d_b
        data = token_d_b.find_one({"token": token_id})
        return data["user"]
# Removed Exception handling from this function


