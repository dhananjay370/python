import mysql.connector
from mysql.connector import Error


class Deposit:
    def __init__(self, accno, amount):
        self.accno = accno
        self.amount = amount

    def deposit(self):
        try:
            connect = mysql.connector.connect(
                host='localhost', user='root', password='password', database='ac')
            cursor = connect.cursor()
            query = f"select balance from accounts where account_no={self.accno};"
            cursor.execute(query)
            balance = cursor.fetchone()[0]
            balance += self.amount
            query = f"update acccounts set balance = {balance} where account_no={self.accno};"
            cursor.execute(query)
            connect.commit()
            print(
                f"Amount Deposited Successfully! Your Balance is Now {balance}")
        except Error as e:
            print(f"The error is {e}")
            

