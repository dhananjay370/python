import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost", user="root", password="password", database="student")

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE bank_account (id INT AUTO_INCREMENT PRIMARY KEY, account_no VARCHAR(255), account_holder VARCHAR(255), balance INT, created_at DATETIME)")

class BankAccount:
    def __init__(self, account_no, account_holder):
        self.account_no = account_no
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        now = datetime.now()
        created_at = now.strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO bank_account (account_no, account_holder, balance, created_at) VALUES (%s, %s, %s, %s)"
        val = (self.account_no, self.account_holder, self.balance, created_at)
        mycursor.execute(sql, val)
        mydb.commit()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            now = datetime.now()
            created_at = now.strftime('%Y-%m-%d %H:%M:%S')
            sql = "INSERT INTO bank_account (account_no, account_holder, balance, created_at) VALUES (%s, %s, %s, %s)"
            val = (self.account_no, self.account_holder,
                   self.balance, created_at)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Amount Withdrawl Successfully...")

    def get_balance(self):
        return self.balance


# account = BankAccount('67549938553', 'Dhananjay Sable')
# account.deposit(1000)
# account.withdraw(500)
# print("Account balance:", account.get_balance())


while True:
    print("To Create Account press (1)")
    print("To Deposit Amount press (2)")
    print("To Withdraw Amount press (3)")
    print("To Quit press (4)")
    user = int(input("Enter Your Option Number : "))
    if user == 1:
        acno = int(input("Enter Your Account Number : "))
        print(f"Your Account No is {acno}")
        name = input("Enter Your Name : ")
        result = BankAccount(acno, name)
        print(f"{name} Your Account is Created Successfully.")
    elif user == 2:
        amount=int(input("Enter Amount for Deposit : "))
        result.deposit(amount)
        print("Amount Deposited Successfully..")
    elif user == 3:
        amountw=int(input("Enter Amount for Withdrawl : "))
        result.withdraw(amountw)
        
    else:
        break
