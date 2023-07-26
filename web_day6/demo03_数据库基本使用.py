"""
作者：张浩
时间：2023/7/25  13:45
邮箱：88302599@qq.com
"""
"""
pip install pymysql
"""

import pymysql

#1、创建数据库链接
conn=pymysql.connect(host="192.168.2.109",
                     user = "root",
                     password="root",
                     port=3306,
                     database = "fire",
                     charset='utf8')

#2、创建一个游标对象
cur = conn.cursor()

#3、执行sql
# sql = "select  * from manager "
#
# res = cur.execute(sql)#返回查询的条数
#
# print(res)

#4 查询结果
#
# sql = "select  * from manager"
# cur.execute(sql)#返回查询的条数
# # res = cur.fetchall()#获取语句的所有结果
# # print("第一次查询",cur.fetchall())#执行结果，只能使用一次，如果想多次使用，请用变量接收
# # print("第二次查询",cur.fetchall())
# # print("第三次查询",cur.fetchall())
#
#
# # res = cur.fetchone()
# print(cur.fetchone())#cur.fetchone()返回查询结果的第一条记录
# print(cur.fetchone())
# print(cur.fetchone())


#5、操作数据（增、删、改）

sql = "update manager set id = 10010 where admin = 'xmy'"
res = cur.execute(sql)#返回SQL语句影响的条数
print(res)
conn.commit()#在执行增、删、改操作语句需要执行该语句



cur.close()
conn.close()