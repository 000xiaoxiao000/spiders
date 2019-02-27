import csv

with open('data.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'qianfg', 20])
    writer.writerow(['10002', 'xiaoxiao', 19])
    writer.writerow(['10003', 'huihui', 22])
    writer.writerow(['10004','nobody',100])

with open('data2.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(['id','name','age'])
    writer.writerows([['10001', 'qianfg', 20],['10002', 'xiaoxiao', 19],['10003', 'huihui', 22]])
#字典写入
with open('data4.csv','w') as f:
    fieldnames=['id', 'name', 'age']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001', 'name':'qianfg','age':20})
with open('data4.csv','a',encoding='utf8') as f:
    fieldnames=['id','name','age']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writerow({'id':'10002','name':'晓晓','age':19})

with open('data4.csv','r',encoding='utf-8') as f:
    reader=csv.reader(f)
    for readline in reader:
        print(readline)

#用pandas打开csv文件
import pandas as pd

df=pd.read_csv('data4.csv')
print(df)