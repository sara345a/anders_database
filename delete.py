from connection import db

db.dishes.delete_one({ "id": 2 })
