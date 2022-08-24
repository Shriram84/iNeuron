import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "loveline123#" )
cursor = mydb.cursor()
cursor.execute("insert into shriram.ineuron1 values( 605, 'shriram', 'shriram@gmail.com', 35000, 30)")
cursor.execute("insert into shriram.ineuron1 values( 608, 'hemanth', 'hemanth@gmail.com', 28000, 30)")
cursor.execute("insert into shriram.ineuron1 values( 620, 'diksha', 'diksha@gmail.com', 27000, 30)")
cursor.execute("insert into shriram.ineuron1 values( 622, 'sonal', 'sona@gmail.com', 31000, 27)")
cursor.execute("insert into shriram.ineuron1 values( 611, 'aniket', 'aniket@gmail.com', 29000, 30)")
mydb.commit()
cursor.execute("select * from shriram.ineuron1")
l= []
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))