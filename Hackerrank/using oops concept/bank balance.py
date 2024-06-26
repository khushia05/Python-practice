class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def debit(self,debit_amt):
        self.balance-=debit_amt
        print(f"{debit_amt} was debited from your account") 
        print("total balance is", self.get_balance())
    def credit(self,credit_amt):
         self.balance+=credit_amt
         print(f"{credit_amt} was credited to your account")
         print("total balance is",self.get_balance())
    def get_balance(self):
        return self.balance     

obj=Account(5000,4336661189999)
obj.debit(500)
obj.credit(200)