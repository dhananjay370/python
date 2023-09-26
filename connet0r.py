import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(
        host="localhost", user="root", password="password", database="student")
    mycursor = connection.cursor()
    # query = "create table randomtable(name varchar(30),rollno int, address varchar(30));"
    # query = "insert into randomtable values('Dhananjay',21,'Shivaji Nagar');"
    # query = "insert into randomtable values('Shubham',22,'Saheb Nagar');"
    # query = "insert into randomtable values('hrishikesh',23,'Aurangabad');"
    # query = "insert into randomtable values('Vijay',24,'Raghav Nagar');"
    mycursor.execute("Select * from randomtable;")
    result=mycursor.fetchall()
    # connection.commit()
    for i in result:
        print(i)
    # print("Record Inserted Successfully.")

    # connection.commit()
    connection.close()
    # if connection.is_connected():
    #     print("Connected Successfully.")
    # else:
    #     print("Connection Unsuccessfull!")

    # connection.commit()
    # connection.close()

except Error as e:
    print(f"The error {e}")
