import mysql.connector
from mysql.connector import Error


class Deposit:
    def __init__(self, account_no, amount):
        self.acno = account_no
        self.amount = amount

    def deposit(self):
        try:
            connect = mysql.connector.connect(
                host="localhost", user="root", password="password", database="ac")
            cursor = connect.cursor()
            sql = f"select balance from accounts where account_no ={self.acno};"
            cursor.execute(sql)
            balance = cursor.fetchone()[0]
            balance += self.amount
            sql = f"update accounts set balance = {balance} where account_no = {self.acno};"
            cursor.execute(sql)
            connect.commit()
            print(f"Deposit of {self.amount} credits Successful")

        except Error as e:
            print(f"{e}")


class Withdrawl:
    def __init__(self, accno, amount):
        self.acno = accno
        self.amount = amount

    def withdrawl(self):
        try:
            connect = mysql.connector.connect(
                host='localhost', user='root', password='password', database='ac')
            cursor = connect.cursor()
            query = f"select balance from accounts where account_no={self.acno};"
            cursor.execute(query)
            balance = cursor.fetchone()[0]
            if balance < self.amount:
                print(f"Insufficient balance")
            else:
                balance -= self.amount
                query = f"update accounts set balance = {balance} where account_no={self.acno};"
                cursor.execute(query)
                connect.commit()
                print(f"Withdrawl of {self.amount} credits Successful")
        except Error as e:
            print(f"{e}")

# ac = Deposit(1011, 500)
# ac.deposit()
ac=Withdrawl(1001,500)
ac.withdrawl()
