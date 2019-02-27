#连接数据库
#关系型数据库MySQL
# import pymysql
# db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306)
# cursor=db.cursor()
# cursor.execute('SELECT VERSION()')      #获取MySQL当前版本
# data=cursor.fetchone()
# print('Database version:',data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')     #创建数据库spiders
# db.close()

#创建数据表students
# import pymysql
# db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306,db='spiders')
# cursor=db.cursor()
# sql='CREATE TABLE IF NOT EXISTS students(id VARCHAR(100) NOT NULL,name VARCHAR(100) NOT NULL,age INT(100) NOT NULL,PRIMARY KEY(id))'
# cursor.execute(sql)
# db.close()

#插入数据
# import pymysql
# id='20120007'
# user='Wuruhui'
# age=25
# db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306,db='spiders')
# cursor=db.cursor()
# sql='INSERT INTO students(id,name,age) VALUES(%s,%s,%s)'
# print(sql)
# try:                                             #插入、更新和删除操作的标准写法
#     if cursor.execute(sql,(id,user,age)):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

#动态插入
# import pymysql
# db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306,db='spiders')
# cursor=db.cursor()
# data={
#     'id':'20120004',
#     'name':'Pipixia',
#     'age':23
# }
# table='students'
# keys=','.join(data.keys())
# values=','.join(['%s']*len(data))
# sql='INSERT INTO {table}({keys}) VALUES({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

#更新数据
# import pymysql
# db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306,db='spiders')
# cursor=db.cursor()
# sql='UPDATE students SET age=%s WHERE name=%s'
# try:
#     cursor.execute(sql,(26,'Bob'))
#     db.commit()
#     print('Successful')
# except:
#     db.rollback()
#     print('Failed')
# db.close()

#去重
# import pymysql
# db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306,db='spiders')
# cursor=db.cursor()
# data={
#     'id':'20120001',
#     'name':'Bob',
#     'age':22
# }
#
# table='students'
# keys=','.join(data.keys())
# values=','.join(['%s']*len(data))
# sql='INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values) #如果主键已存在，就执行更新操作
# print(sql)
# update=','.join(['{key}=%s'.format(key=key) for key in data])
# print(update)
# sql+=update
# print(sql)
# print(tuple(data.values())*2)
# try:
#     if cursor.execute(sql,tuple(data.values())*2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

#删除数据
# import pymysql
# db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306,db='spiders')
# cursor=db.cursor()
# table='students'
# condition='age>18'
# sql='DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
# print(sql)
# try:
#     if cursor.execute(sql):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

#查询数据
# import pymysql
# db=pymysql.connect(host='localhost',user='root',password='qfg2871445718',port=3306,db='spiders')
# cursor=db.cursor()
# sql='SELECT * FROM students WHERE age>20'
# try:
#     cursor.execute(sql)
#     print('Count:',cursor.rowcount)
#     one=cursor.fetchone()
#     print('One:',one)
#     results=cursor.fetchall()
#     print('Results:',results)
#     print('Results Type:',type(results))
#     for row in results:
#         print(row)
# except:
#     print('Error')