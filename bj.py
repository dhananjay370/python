class BankAccount:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def deposit(self, deposit):
        self.balance += deposit

    def withdraw(self, withdraw):
        self.balance -= withdraw

    def getbalance(self):
        print(f"Current Balance is : {self.balance}")


class Withdrawl:
    def ac(self, pin, balance):
        while not isinstance(pin, str) or len(pin) != 4 or not pin.isdigit():
            pin = input("Enter Your 4 digit Pin : ")
        if pin == BankAccount.pin:
            cash = int(input("Enter Ammount : "))
            if cash > balance:
                print("Insufficient Balance!")
            else:
                print(f"Collect Your Cash {cash}.")
                return True
        else:
            print("Wrong Pin!")
            return False


ac = BankAccount(50000, "3333")
wd = Withdrawl()
user = 0
while user != 5:
    user = int(input(
        "1. Cash Withdrawl\t2. Cash Deposit\n3. Current Balance\t4. Pin Change\n5. Quit.\n\nEnter Option Number : "))
    if user == 1:
        if wd.ac(ac.pin, ac.balance):
            break
    elif user == 2:
        deposit = int(input("Enter deposit amount: "))
        ac.deposit(deposit)
    elif user == 3:
        ac.getbalance()
    elif user == 4:
        old_pin = input("Enter your old 4-digit PIN: ")
        while not isinstance(old_pin, str) or len(old_pin) != 4 or not old_pin.isdigit() or old_pin != BankAccount.pin:
            old_pin = input("Invalid PIN. Enter your old 4-digit PIN: ")
        new_pin = input("Enter your new 4-digit PIN: ")
        while not isinstance(new_pin, str) or len(new_pin) != 4 or not new_pin.isdigit():
            new_pin = input("Invalid PIN. Enter a 4-digit PIN: ")
        BankAccount.pin = new_pin
        print("PIN changed successfully.")
    elif user == 5:
        print("Quitting.")
