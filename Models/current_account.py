from Models.bank_account import BankAccount
from Utils.exceptions import InvalidAmountError,OverdraftError
class CurrentAccount(BankAccount):
    def __init__(self, name, account_number, account_type, phone_number,overdraft_limit,balance=0):
        super().__init__(name, account_number, account_type, phone_number,balance)
        self.overdraft_limit=overdraft_limit
    def withdraw(self, amount):
        if amount<=0:
            raise InvalidAmountError("Invalid Amount")
        if amount>(self.balance+self.overdraft_limit):
            raise OverdraftError("Insufficient available funds for this transaction.")
        else:
            self.balance-=amount
