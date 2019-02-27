import pymongo

KEYWORD='拟茎点霉属'

MONGO_URL='localhost'
MONGO_DB='CNKI'
MONGO_COLLECTION=KEYWORD
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
collection=db[MONGO_COLLECTION]
result=collection.find_one({'title':'拟茎点霉属及其病害研究进展'})
print(type(result))
print(result['download'])