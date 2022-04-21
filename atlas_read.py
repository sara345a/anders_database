from connection_atlas import db


dishes_cursor = db.dishes.find()

dishes = [dish for dish in dishes_cursor]

print(dishes)