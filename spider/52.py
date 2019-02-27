import pymysql
db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306)
cursor=db.cursor()
cursor.execute('SELECT VERSION()')
data=cursor.fetchone()
print('Database version:',data)
db.close()