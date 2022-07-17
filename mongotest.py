import pymongo

client = pymongo.MongoClient("mongodb+srv://Anurag:Password1@anurag.jx9b7.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"Anurag",
    "email":"anurag1@abc",
    "surname":"gupta"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
