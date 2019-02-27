#文本存储
# txt文本存储
# import requests
# from pyquery import PyQuery as pq
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# html=requests.get('http://www.zhihu.com/explore',headers=headers).text
# doc=pq(html)
# items=doc('.explore-feed.feed-item').items()
# for item in items:
#     question=item.find('h2').text()
#     print(question)
#     author=item.find('.author-link').text()
#     print(author)
#     content=pq(item.find('.content').html()).text()   #pq初始化为HTML文本，再利用text()返回纯文本
#     print(content)
#     with open('explore.txt','a',encoding='utf-8') as f:     #utf-8编码
#         f.write('\n'.join([question,author,content]))
#         f.write('\n'+'*'*100+'\n')

#json文件存储    JSON数据要用双引号""包裹
#读取
import json
# str='''
# [{
# "name":"Mike",
# "gender":"male",
# "age":"20"
# },{
# "name":"Selina",
# "gender":"female",
# "age":"18"
# }]
# '''
# print(type(str))
# data=json.loads(str)
# print(data)
# print(type(data))
# print(data[0].get('name'))
# with open('data.json','r') as f:
#     str=f.read()
#     data=json.loads(str)
#     print(data)

#输出
# import json
# data2=[{
# "name":"Mike",
# "gender":"male",
# "age":"20"
# },{
# "name":"Selina",
# "gender":"female",
# "age":"18"
# }]
# with open('data2.json','w') as f:
#     f.write(json.dumps(data2))       #将json对象转为字符串
# data3=[{
# "name":"皮皮虾",
# "gender":"男",
# "age":"20"
# },{
# "name":"Selina",
# "gender":"female",
# "age":"18"
# }]
# with open('data3.json','w',encoding='utf-8') as f:
#     f.write(json.dumps(data3,indent=2,ensure_ascii=False))      #ensure_ascii=False防止中文字符变为Unicode字符

#CSV文件存储
#写入
# import csv
# with open('data.csv','w',newline='') as f:      #newline=''防止出现个空白行
#     writer=csv.writer(f)
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','Bob',20])
#     writer.writerow(['10002','Mike',22])
#     writer.writerow(['10003','Selina',18])

# import csv
# with open('data2.csv','w',newline='') as f:
#     writer=csv.writer(f,delimiter=' ')      #delimiter修改分隔符
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','Bob',20])
#     writer.writerow(['10002','Mike',22])
#     writer.writerow(['10003','Selina',18])

#字典写入
# import csv
# with open('data3.csv','w',newline='')as f:
#     fieldnames=['id','name','age']
#     writer=csv.DictWriter(f,fieldnames=fieldnames)      #初始化
#     writer.writeheader()                                #写入头信息
#     writer.writerow({'id':'10001','name':'Bob','age':22})
#     writer.writerow({'id': '10002', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 18})

#追加写入
# import csv
# with open('data3.csv','a',newline='') as f:
#     fieldnames=['id','name','age']
#     writer=csv.DictWriter(f,fieldnames=fieldnames)
#     writer.writerow({'id':'10004','name':'pipixia','age':18})

#读取
# import csv
# with open('data3.csv','r',encoding='utf-8') as f:
#     reader=csv.reader(f)
#     for row in reader:
#         print(row)
# #pandas读取
# import pandas
# pd=pandas.read_csv('data3.csv')
# print(pd)

