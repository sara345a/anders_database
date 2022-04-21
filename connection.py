from pymongo import MongoClient

CONNECTION_STRING = "mongodb://localhost:27017"
DB_NAME = "food"


client = MongoClient(CONNECTION_STRING)


db = client[DB_NAME]

