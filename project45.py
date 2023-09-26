class Account:
    def __init__(self,balance):
        self.balance=balance
    
    def deposit(self,amount):
        self.amount=amount
        if self.balance<=0:
           self. balance+=amount
           print("amount is Successful.. deposit")
        else:
            print(" amount not deposit")
           
       
    def withdrawal(self,amount):
        self.amount=amount
        if self.balance>=0:
            self.balance-=amount
            print("amount is Successful.. withdrawal")
        else:
            print("amount in not withdrawal")
    def check(self):
        print(f"Balance : {self.balance}")    
ac=Account(0)
ac.deposit(100000)

ac.withdrawal(80000)
ac.check()

ac.deposit(9999)
ac.withdrawal(80000)
ac.check()           