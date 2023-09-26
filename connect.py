import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="password", database="student")

    mycursor = mydb.cursor()
    mycursor.execute(
        "create table custume(rollno int primary key,name varchar(30),Division varchar(1);")

    myresult = mycursor.fetchall()
  
    for x in myresult:
        print(x)

    mydb.commit()
    # b = mydb.is_connected()
    # print(b)

    mydb.close()

except Error as e:
    print(f"Error is {e}")
