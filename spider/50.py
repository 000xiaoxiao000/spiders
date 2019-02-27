import json

content='''
[{
    "name":"钱富根",
    "gender":"男",
    "birthday":"1995-01-01"},{
    "name":"xiaoxiao",
    "gender":"female",
    "birthday":"1997-01-01"
    }]
'''
'''print(type(content))
data=json.loads(content)
print(data)
print(type(data))
print(data[0].get('name'))'''

print(type(content))
data=json.loads(content)
print(data)
print(type(data))
print(data[1].get('pipixia',666))
with open('content.json','w',encoding='utf-8') as f:
    f.write(json.dumps(content,indent=2,ensure_ascii=False))