import mysql.connector
from mysql.connector import Error



print("---------------Welcome To Bank---------------\n")
print("1. Create Account\t2. Deposit Amount\n3. Withdrawl Amount\t4 Quit\n")
choose = int(input("Enter Your Option Number : "))
if choose > 4:
    print("Invalid Option Number")
    exit()
if choose == 1:
    name = input("Enter Your Name : ")
    account_Type=input("Account Type : ")
    balance = int(input("Note! Deposit Amount Should Greater Than 500 RS\nDeposit Amount : "))
    if balance < 500:
        print("Balance Should Greater Than 500 RS!")

    
# class Account:
#     def __init__(self, name, account_type, balance):
#         self.account_no = 1001
#         self.name = name
#         self.account_type = account_type
#         self.balance = balance
#         self.account_no = self.account_no + 1

#     def openaccount(self):
#         try:
#             connect = mysql.connector.connect(
#                 host="localhost", user="root", password="password", database="ac")
#             cursor = connect.cursor()

#             cursor.execute('select * from accounts;')
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#         except Error as e:
#             print(f"Error is {e}")


# ac = Account()
