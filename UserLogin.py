import re
import mysql.connector
from mysql.connector import Error

try:
    connect = mysql.connector.connect(
        host="localhost", user="root", password="password", database="accounts")
    cursor = connect.cursor()

except Error as e:
    print(f"Error is {e}")


class Account:
    def userlogin(self, username, password):
        self.username = username
        self.password = password
        sql = f"insert into userlogin values('{self.username}','{self.password}');"
        cursor.execute(sql)
        connect.commit()
        connect.close()


def is_strong_password(password):

    if len(password) < 8:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[!@#$%^&*]", password):
        return False

    return True


ac = Account()

while True:

    username = input("Enter Your User Name : ")
    password = input("Enter Your Password : ")
    if password != is_strong_password(password) == False:
        print("Week Password!")
    if len(username) >= 10 and is_strong_password(password) == True:
        ac.userlogin(username, password)
        print("Login details saved successfully..")
        break
    else:
        print("Note!\nUsername should be greater than minimum 10 digits and Password should be Strong and greater than minimum 8 digits!")
        print("Please Try Again!")
