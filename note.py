import mysql.connector
from mysql.connector import Error
try:
    acn = input("Enter Account No.")
    nam = input("Enter Name ")
    bal = input("Enter Balance ")
    connection = mysql.connector.connect(
        host="localhost", user="root", password="password", database="student")
    cursor = connection.cursor()
    cursor.execute(f"insert into account values({acn},'{nam}',{bal});")
    result=cursor.fetchall()
    for i in result:
        print(i)
    connection.commit()
    print("data saved...")
    connection.close()
except Error as e:
    print(f"Error :{e}")
