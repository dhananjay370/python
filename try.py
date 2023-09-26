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


ac = Account()

while True:

    username = input("Enter Your User Name : ")
    password = input("Enter Your Password : ")

    if len(username) >= 10 and len(password) >= 8:
        ac.userlogin(username, password)
        print("Login details saved successfully..")
        break
    elif len(username) < 10 and len(password) < 8:
        print("Note!\nUsername should be greater than minimum 10 digits and Password should be greater than minimum 8 digits!")
        print("Please Try Again!")
