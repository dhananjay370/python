import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="password", database="student")

mycursor = mydb.cursor()
# mycursor.execute("create table mydata(FullName varchar(30), rollNo int, course varchar(30));")
# mycursor.execute("insert into mydata values('Dhananjay',01, 'Python');")
mycursor.execute("insert into mydata values('Shubham',02, 'Python');")
# mycursor.execute("drop table mydata;")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
