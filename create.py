from dis import dis
from connection import db

dish_to_insert = {
    "name": "Fried Chicken",
    "price": 50
}

insertion_result = db.dishes.insert_one(dish_to_insert)

print(insertion_result)


