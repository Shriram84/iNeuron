import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "loveline123#" )
cursor = mydb.cursor()
cursor.execute("select employe_id, emp_salary from shriram.ineuron1")
for i in cursor.fetchall():
    print(i)
