import pymysql

data={
    'id':'20120001',
    'name':'Bob',
    'age':20
}
db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306,db='spiders')
cursor=db.cursor()
table='students'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql='INSERT INTO {table}({keys}) VALUES({values})'.format(table=table,keys=keys,values=values)
try:
    if cursor.exectue(sql,tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()