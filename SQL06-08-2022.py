import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "loveline123#" )
cursor = mydb.cursor()
cursor.execute("create database August06")
#cursor.execute("show databases")
#cursor.execute("create table August06.practice(customer_id int(10), title varchar(80), staff_id int(10), sales int(10))")
#cursor.execute("insert into August06.practice values( 605, 'Sholay', 2, 2300 )")
#cursor.execute("insert into August06.practice values( 610, 'RHTDM', 1, 5400 )")
#cursor.execute("insert into August06.practice values( 622, 'Lagaan', 2, 6500 )")
#cursor.execute("insert into August06.practice values( 612, 'DDLJ', 1, 8200 )")
mydb.commit()
cursor.execute("select * from August06.practice")
print(cursor.fetchall())