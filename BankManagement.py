import mysql.connector
from mysql.connector import Error


class OpenAcc:
    def __init__(self, account_no, usrname, acctype, balance):
        self.account_no = account_no
        self.usrname = usrname
        self.acctype = acctype
        self.balance = balance

    def openacc(self):
        try:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="password", database="ac")
            cursor = connect.cursor()
            q1 = f"insert into accounts values({self.account_no},'{self.usrname}','{self.acctype}',{self.balance});"
            cursor.execute(q1)
            connect.commit()
        except Error as e:
            print(f"{e}")


class Register:
    def __init__(self, username, password, account_no):
        self.username = username
        self.password = password
        self.account_no = account_no

    def register(self):
        try:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="password", database="ac")
            cursor = connect.cursor()
            query = f"insert into credentials values('{self.username}','{self.password}','{self.account_no}');"
            query2 = f"select account_no from credentials;"
            cursor.execute(query2)
            rows = cursor.fetchone()[0]
            if rows:
                print("User Already Existed!")
            else:
                cursor.execute(query)
                connect.commit()
                print(f"{self.username} Registered Successfully.")
        except Error as e:
            print(f"{e}")


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        try:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="password", database="ac")
            cursor = connect.cursor()
            query = f"select * from credentials where username = '{self.username}' and password = '{self.password}'"
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                print(f"{self.username} is logged in")
            else:
                print("Invalid Username Password!")
        except Error as e:
            print(f"{e}")


class Deposit:
    def __init__(self, account_no, amount):
        self.account_no = account_no
        self.amount = amount

    def deposit(self):
        try:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="password", database="transactions")
            cursor = connect.cursor()
            query1 = f"select balance from transactions where account_no = {self.account_no};"
            cursor.execute(query1)
            balance = cursor.fetchone()[0]
            balance += self.amount
            query2 = f"update transactions set balance = {balance} where account_no = {self.account_no};"
            cursor.execute(query2)
            connect.commit()
            print(
                f"Amount Deposited Successfully.\nYour Balance is Now {balance}")
        except Error as e:
            print(f"{e}")


class Withdrawl:
    def __init__(self, account_no, amount):
        self.account_no = account_no
        self.amount = amount

    def withdrawl(self):
        try:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="password", database="transactions")
            cursor = connect.cursor()
            query1 = f"select balance from transactions where account_no = {self.account_no};"
            cursor.execute(query1)
            balance = cursor.fetchone()[0]
            if balance < self.amount:
                print("Insufficient Balance!")
            else:
                balance -= self.amount
                query2 = f"update transactions set balance = {balance} where account_no = {self.account_no};"
                cursor.execute(query2)
                connect.commit()
                print("Amount Withdrawl Successfully.")
                print(f"Your Balance is {balance}")
        except Error as e:
            print(f"{e}")


class Transfer:
    def __init__(self, account_no, amount, account_no_to):
        self.account_no = account_no
        self.amount = amount
        self.account_no_to = account_no_to

    def transfer(self):
        try:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="password", database="transactions")
            cursor = connect.cursor()
            query1 = f"select balance from transactions where account_no = {self.account_no};"
            cursor.execute(query1)
            balance = cursor.fetchone()[0]

            if balance < self.amount:
                print("Insufficient Balance!")
            else:
                balance -= self.amount
                query2 = f"update transactions set balance = {balance} where account_no = {self.account_no};"
                cursor.execute(query2)
                connect.commit()
                query3 = f"select balance from transactions where account_no = {self.account_no_to};"
                cursor.execute(query3)
                balance_to = cursor.fetchone()[0]
                balance_to += self.amount
                query4 = f"update transactions set balance = {balance_to} where account_no = {self.account_no_to};"
                cursor.execute(query4)
                connect.commit()
                print("Amount Transfer Successfully.")
                print(f"Your Balance is {balance}")
                print(f"Your Balance is {balance_to}")

        except Error as e:
            print(f"{e}")


if __name__ == "__main__":
    print("Welcome to Banking System.")
    print('1. Register\t2. Open Account\n3. Deposit\t4. Withdrawl\n5. Transfer\t6. Quit.')
    option = int(input("Enter Your Option : "))
    if option == 1:
        username = input("Enter Your Username : ")
        password = input("Enter Your Password : ")
        account_no = int(input("Enter Your Account No : "))
        objlogin = Register(username, password, account_no)
        objlogin.register()
    elif option == 2:
        username = input("Enter Your Username : ")
        password = input("Enter Your Password : ")
        account_no = int(input("Enter Your Account No : "))
        objlogin = Login(username, password, account_no)
        objlogin.login()
    elif option == 3:
        account_no = int(input("Enter Your Account No : "))
        amount = int(input("Enter Amount : "))
        objdeposit = Deposit(account_no, amount)
        objdeposit.deposit()
    elif option == 4:
        account_no = int(input("Enter Your Account No : "))
        amount = int(input("Enter Amount : "))
        objwithdraw = Withdrawl(account_no, amount)
        objwithdraw.withdrawl()
    elif option == 5:
        account_no = int(input("Enter Your Account No : "))
        account_no_to = int(input("Enter Your Account No To : "))
        amount = int(input("Enter Amount : "))
        objtransfer = Transfer(account_no, amount, account_no_to)
    else:
        print("Thank You For Using our Project.")