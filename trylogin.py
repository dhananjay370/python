import mysql.connector
from mysql.connector import Error
import getpass
import msvcrt

try:
    connect = mysql.connector.connect(
        host="localhost", user="root", password="password", database="accounts")
    cursor = connect.cursor()

except Error as e:
    print(f"The Error is {e}")
    
def masked_input(prompt='Password: '):
    password = ''
    while True:
        ch = msvcrt.getch().decode('utf-8')
        if ch == '\r' or ch == '\n':
            break
        password += ch
        print('*', end='', flush=True)
    print()
    return password


class Login:
    def getLogin(self):
        username = input("Enter Your Username : ")
        password = masked_input(prompt="Enter Your Password : ")
        cursor.execute(
            "select * from userlogin where username = %s and password = %s", (username, password))
        rows = cursor.fetchall()
        if rows:
            print("Login Successful..")
            connect.commit()
            connect.close()
            exit()
        else:
            print("Invalid username and password!")

log = Login()
log.getLogin()
