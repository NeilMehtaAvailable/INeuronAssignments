import pymongo

client = pymongo.MongoClient("mongodb+srv://neilmehta429:Samsung123#@cluster0.3ihwv4e.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "neil",
    "email":"gmail",
    "surname": "mehta"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)