import mysql.connector
from mysql.connector import Error
import getpass


class TryLogin:
    def login(self):
        try:
            connect = mysql.connector.connect(
                host='localhost', user='root', password='password', database='accounts')
            cursor = connect.cursor()
            username = input("Enter Your Username : ")
            password = getpass.getpass(prompt="Enter Your Password : ")

            cursor.execute(
                "select * from userlogin where username = %s and password = %s", (username, password))

            rows = cursor.fetchall()
            if rows:
                print('Login Successfully..')
                connect.commit()
                connect.close()
            else:
                print('Login Unsuccessfull!')
                connect.close()
        except Error as e:
            print(f"Error is : {e}")


openac = TryLogin()
openac.login()
