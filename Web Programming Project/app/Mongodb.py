import pymongo

#mongodb sample data
client = pymongo.MongoClient("mongodb+srv://Nithin:Nithin007@cluster0.3mubmvh.mongodb.net/?retryWrites=true&w=majority")
mongoDB = client.sample_restaurants
neighcol= mongoDB.neighborhood
restaurantscol= mongoDB.restaurants
restaurants = list(restaurantscol.find({}))