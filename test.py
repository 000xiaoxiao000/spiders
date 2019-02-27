import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017')
db=client['product']
collection=db['ipad']
count=collection.find().count()
print(count)

