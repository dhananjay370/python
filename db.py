import mysql.connector
from mysql.connector import Error

try:
    connect = mysql.connector.connect(host="root",)
    
except Error as e:
    print(e)