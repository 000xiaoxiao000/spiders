#连接MongoDB
import pymongo
client=pymongo.MongoClient(host='localhost',port=27017)
# client=pymongo.MongoClient('mongodb://localhost:27017/')
#指定数据库
db=client['test']
#指定集合
collection=db['students']
#插入数据  insert,insert_one,insert_many
# student1={
#     'id':'20170001',
#     'name':'Bob',
#     'age':20,
#     'gender':'male'
# }
# student2={
#     'id':'20170002',
#     'name':'Jack',
#     'age':21,
#     'gender':'male'
# }
# student3={
#     'id':'20170003',
#     'name':'Selina',
#     'age':20,
#     'gender':'female'
# }
# result=collection.insert([student1,student2,student3])
# print(result)
#查询 find,find_one
# result=collection.find_one({'name':'Bob'})
# print(type(result))
# print(result)

#根据ObjectId查询
# from bson.objectid import ObjectId
# result=collection.find_one({'_id': ObjectId('5b778c7077bd7a2488c83a95')})
# print(result)
# results=collection.find({'age':20})
# print(results)
# for result in results:
#     print(result)

#根据比较符号查询
# results=collection.find({'age':{'$lt':26}})
# for result in results:
#     print(result)

#根据正则匹配查询
# results=collection.find({'name':{'$regex':'^B.*'}})
# print(results)
# for result in results:
#     print(result)

#计数 count
# count=collection.find().count()
# print(count)

#排序 sort
# results=collection.find().sort('name',pymongo.ASCENDING)        #升序用ASCENDING，降序用DESCENDING
# print([result['name'] for result in results])

#偏移 skip
# results=collection.find().sort('name',pymongo.DESCENDING).skip(2)
# print([result['name'] for result in results])
#限制个数
# results=collection.find().sort('name',pymongo.DESCENDING).skip(2).limit(4)
# print([result['name'] for result in results])
#千万、亿级别数据库，防止内存溢出,使用_id查询
# from bson.objectid import ObjectId
# collection.find({'_id':{'$lt':ObjectId('5b778f4877bd7a1388e0f7ce')}})

#更新
# condition={'name':'huihui'}
# student=collection.find_one(condition)
# print(student)
# student['age']=18
# result=collection.update(condition,student)
# print(result)

#删除
condition={'age':20}
result=collection.remove(condition)
print(result)


