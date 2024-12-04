

# bank[ac no,balance,ac_type,customer name]  [initialize,deposit(amount),withdraw(amount),get_balance()]


class Bank:

    account_no:int

    balance:int

    ac_type:str

    customer_name:str

    def __init__(self,account_no,balance,ac_type,customer_name):

        self.account_no=account_no

        self.balance=balance

        self.ac_type=ac_type

        self.customer_name=customer_name

    def deposit(self,amount):

        self.balance+=amount

        print(f"your account{self.account_no} has been credited with amount {amount} avl balance is {self.balance}")

    def withdraw(self,amount):

        if self.balance>=amount:

            self.balance-=amount

            print(f"your account{self.account_no} has been debited with amount {amount} avl balance is {self.balance}")
        else:
            print("insufficient balance")

    def get_balance(self):

        print("your avl balance",self.balance)
        
        

bank_instance=Bank(47563872,2500,"savings","Anu")

bank_instance.get_balance()
