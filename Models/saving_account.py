from Models.bank_account import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self,name,account_number,account_type,phone_number,interest_rate,balance=0):
        super().__init__(name,account_number,account_type,phone_number,balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        balance=(self.balance*self.interest_rate)/100
        self.deposit(balance)
    




