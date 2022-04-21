from connection import db

# This is the cursor.. we now need to iterate over it
dishes_cursor = db.dishes.find()

# for dish in dishes_cursor:
#     print(dish)

dishes = [dish for dish in dishes_cursor]

print("This is the list", dishes)
