class BankAccount:
    def b(self, balance):
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, withdraw):
        self.balance -= withdraw

    def getbalance(self):
        print(f"Current Balance is : {self.balance}")


pins = 3333


class Withdrawl:
    def ac(self, pin, cash):
        self.pin = pin
        cash = int(input("Enter Ammount : "))
        if cash > BankAccount.b:
            print("Insufficient Balance!")
        pin = int(input("Enter Your 4 digit Pin : "))
        while len(pin) != 4 or not pin.isdigit():
            pin = input("Invalid PIN. Enter a 4-digit PIN: ")
            if pin == pins:
                print(f"Collect Your Cash {cash}.")


user = 0
ac = BankAccount(50000)
pin = Withdrawl()
while user != 5:
    user = int(input(
        "1. Cash Withdrawl\t2. Cash Deposit\n3. Current Balance\t4. Pin Change\n5. Quit.\n\nEnter Option Number : "))
    if user == 1:
        pin.ac(500,0)