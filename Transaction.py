import mysql.connector
from mysql.connector import Error


class Deposit:
    def __init__(self, accno, amount):
        self.accno = accno
        self.amount = amount

    def deposit(self):
        try:
            con = mysql.connector.connect(
                host='localhost', user='root', password='password', database='ac')
            c = con.cursor()
            qf = f"select balance from accounts where account_no={self.accno};"
            c.execute(qf)
            bal = c.fetchone()[0]
            bal += self.amount
            q1 = f"update accounts set balance={bal} where account_no={self.accno};"
            c.execute(q1)
            con.commit()
            print(f"Amount Deposited Successfully. Your New Balance is {bal}")
        except Error as e:
            print(f"Error is : {e}")


class Withdrawal:
    def __init__(self, accno, amount):
        self.accno = accno
        self.amount = amount

    def withdraw(self):
        try:
            con = mysql.connector.connect(
                host='localhost', user='root', password='password', database='ac')
            c = con.cursor()
            qf = f"select balance from accounts where account_no={self.accno};"
            c.execute(qf)
            bal = c.fetchone()[0]
            if bal < self.amount:
                print("Insufficient Balance")
                return
            bal -= self.amount
            q1 = f"update accounts set balance={bal} where account_no={self.accno};"
            c.execute(q1)
            con.commit()
            print(f"Amount Withdrawn Successfully. Your New Balance is {bal}")
        except Error as e:
            print(f"Error is : {e}")


class Withdrawl:
    def __init__(self, accno, amount):
        self.accno = accno
        self.amount = amount

    def withdraw(self):
        try:
            con = mysql.connector.connect(
                host='localhost', user='root', password='password', database='ac')
            c = con.cursor()
            qf = f"select balance from accounts where account_no={self.accno};"
            c.execute(qf)
            balance = c.fetchone()[0]
            if balance < self.amount:
                print("Insufficient Balance")
                return
            balance -= self.amount
            q1 = f"update accounts set balance={balance} where account_no={self.accno};"
            c.execute(q1)
            con.commit()
            print(
                f"Amount Withdrawn Successfully. Your Balance is Now {balance}")
        except Error as e:
            print(f"Error is : {e}")
            
w=Withdrawal(1001,500)
w.withdraw()