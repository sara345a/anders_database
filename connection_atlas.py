from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://root:password1234@cluster0.ids2i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

DB_NAME = "food"


client = MongoClient(CONNECTION_STRING)


db = client[DB_NAME]

