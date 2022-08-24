import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "loveline123#")
print(mydb)
cursor = mydb.cursor()
cursor.execute("create database rama")
cursor.execute("show databases")
print(cursor.fetchall())

#connection established between mysql database & python
