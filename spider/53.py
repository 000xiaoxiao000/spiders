import pymysql

db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306,db='spiders')
cursor=db.cursor()
sql='CREATE TABLE IF NOT EXISTS stdents (id VARCHAR(100) NOT NULL,name VARCHAR(100) NOT NULL,age INT NOT NULL,PRIMARY KEY(id))'
cursor.execute(sql)
db.close()