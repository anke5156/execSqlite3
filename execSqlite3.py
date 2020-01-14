#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@author:    anke
@contact:   anke.wang@foxmail.com
@file:      execSqlite3.py
@time:      2020/1/14 3:24 PM

@desc:    Python操作sqlite3数据库 https://www.runoob.com/sqlite/sqlite-python.html  
'''
import sqlite3

# 连接数据库
# 下面的 Python 代码显示了如何连接到一个现有的数据库。如果数据库不存在，那么它就会被创建，最后将返回一个数据库对象。
conn = sqlite3.connect('./testDB.db')
print("Opened database successfully")
c = conn.cursor()

# 创建表
# 下面的 Python 代码段将用于在先前创建的数据库中创建一个表：
# c.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print("Table created successfully")
# conn.commit()
# conn.close()

# INSERT 操作
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
# print("Records created successfully")
# conn.commit()
# conn.close()

# SELECT 操作
# 下面的 Python 程序显示了如何从前面创建的 COMPANY 表中获取并显示记录：
# cursor = c.execute("SELECT id, name, address, salary  FROM COMPANY")
# for row in cursor:
#     print(row)
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("ADDRESS = ", row[2])
#     print("SALARY = ", row[3], "\n")
#
# print("Operation done successfully")
# conn.close()

# UPDATE 操作
# 下面的 Python 代码显示了如何使用 UPDATE 语句来更新任何记录，然后从 COMPANY 表中获取并显示更新的记录：
# c.execute("UPDATE COMPANY SET SALARY = 25000.00 WHERE ID=1")
# conn.commit()
# print("Total number of rows updated :", conn.total_changes)
#
# cursor = conn.execute("SELECT id, name, address, salary  FROM COMPANY")
# for row in cursor:
#     print(row)
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("ADDRESS = ", row[2])
#     print("SALARY = ", row[3], "\n")
#
# print("Operation done successfully")
# conn.close()

# DELETE 操作
# 下面的 Python 代码显示了如何使用 DELETE 语句删除任何记录，然后从 COMPANY 表中获取并显示剩余的记录：
c.execute("DELETE FROM COMPANY WHERE ID=2;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  FROM COMPANY")
for row in cursor:
    print(row)
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()
