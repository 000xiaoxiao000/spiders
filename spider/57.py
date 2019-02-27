import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
'''
student1={
    'id':'20170101',
    'name':'qianfg',
    'age':22,
    'gender':'male'
}
student2={
    'id':'20170102',
    'name':'huihui',
    'age':25,
    'gender':'female'
}
student3={
    'id':'20170103',
    'name':'xiaoxiao',
    'age':22,
    'gender':'female'
}

#result=collection.insert([student1,student2])
#print(result)
#推荐使用
result=collection.insert_many([student1,student2])
print(result)
print(result.inserted_ids)

result=collection.find_one({'name':'huihui'})
print(type(result))
print(result)

esult=collection.insert_one(student3)
print(result)
#from bson.objectid import ObjectId
#result=collection.find_one({'_id':ObjectId('5b56d87177bd7a183ce37715')})
#print(result)

results=collection.find({'age':{'$type':'int'}})
print(results)
for result in results:
    print(result)

results=collection.find().sort('name',pymongo.ASCENDING).skip(5).limit(2)
print([result['name'] for result in results])

condition={'name':'qianfg'}
student=collection.find_one(condition)
student['age']=22
result=collection.update(condition,student)
print(result)'''

results=collection.find({'name':{'$regex':'^x'}})
print(results)
for result in results:
    print(result)

result=collection.remove({'name':'xiaoxiao'})
print(result)