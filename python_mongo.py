import pymongo
connection = pymongo.MongoClient("null", 00000,
                                username="null",
                                password="null", #pls don't blackmail through this
                                authSource="null")

collection = connection["null"]["listings"]

docs = collection.find(
    {
        "neighbourhood_cleansed": "Södermalms",
        "beds": {"$gt": 2},
        "review_scores_rating": {"$ne": '', "$ne": "null"}
    },
    {
        "_id": 0,
        "name": 1,
        "beds": 1,
        "review_scores_rating": 1,
        "price": 1
    }
).sort("review_scores_rating", -1)

for i in docs:
    print(i)
