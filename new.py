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
                host="localhost", user="root", password="password", database="bank")
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
                host="localhost", user="root", password="password", database="bank")
            cursor = connect.cursor()
            query = f"insert into accounts values('{self.username}','{self.password}','{self.account_no}');"
            query2 = f"select account_no from accounts;"
            cursor.execute(query2)
            rows = cursor.fetchone()
            if rows:
                print("User Already Existed!")
                # exit()
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
                host="localhost", user="root", password="password", database="bank")
            cursor = connect.cursor()
            query = f"select * from accounts where username = '{self.username}' and password = '{self.password}'"
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
                host="localhost", user="root", password="password", database="bank")
            cursor = connect.cursor()
            query1 = f"select balance from accounts where account_no = {self.account_no};"
            cursor.execute(query1)
            balance = cursor.fetchone()[0]
            balance += self.amount
            query2 = f"update accounts set balance = {balance} where account_no = {self.account_no};"
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
                host="localhost", user="root", password="password", database="bank")
            cursor = connect.cursor()
            query1 = f"select balance from accounts where account_no = {self.account_no};"
            cursor.execute(query1)
            balance = cursor.fetchone()[0]
            if balance < self.amount:
                print("Insufficient Balance!")
            else:
                balance -= self.amount
                query2 = f"update accounts set balance = {balance} where account_no = {self.account_no};"
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
                host="localhost", user="root", password="password", database="bank")
            cursor = connect.cursor()
            query1 = f"select balance from accounts where account_no = {self.account_no};"
            cursor.execute(query1)
            balance = cursor.fetchone()[0]

            if balance < self.amount:
                print("Insufficient Balance!")
            else:
                balance -= self.amount
                query2 = f"update accounts set balance = {balance} where account_no = {self.account_no};"
                cursor.execute(query2)
                connect.commit()
                query3 = f"select balance from accounts where account_no = {self.account_no_to};"
                cursor.execute(query3)
                balance_to = cursor.fetchone()[0]
                balance_to += self.amount
                query4 = f"update accounts set balance = {balance_to} where account_no = {self.account_no_to};"
                cursor.execute(query4)
                connect.commit()
                print("Amount Transfer Successfully.")
                print(f"Your Balance is {balance}")
                print(f"Your Balance is {balance_to}")

        except Error as e:
            print(f"{e}")


if __name__ == "__main__":
    print("Welcome to Banking System.")
    # print("Please select an option.")
    # print("1. Login.")
    # print("2. Register.")
    # print("3. Deposit.")
    # print("4. Withdraw.")
    # print("5. Transfer.")
    # print("6. Exit.")
    # choice = int(input("Enter your choice: "))
    # if choice == 1:
    username = input("Enter Your Username : ")
    password = input("Enter Your Password : ")
    account_no = int(input("Enter Your Account No : "))
    objlogin = Register(username, password, account_no)
    objlogin.register()
    # elif choice == 2:
    #     register()
    # elif choice == 3:
    #     deposit()
    # elif choice == 4:
    #     withdraw()
    # elif choice == 5:

    #     transfer()

    # elif choice == 6:
    #     print("Thank you for using Banking System.")
    #     exit()
    # else:
    #     print("Invalid Choice.")
    #     main()
