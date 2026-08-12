# CurrentAccount INHERITS from BankAccount
# Key difference: allows withdrawals beyond balance up to an overdraft limit

from Models.bank_account import BankAccount
from Utils.exceptions import InvalidAmountError, OverdraftError

class CurrentAccount(BankAccount):
    def __init__(self, name, account_number, account_type, phone_number, overdraft_limit, balance=0):
        
        # super() passes the common details to BankAccount's __init__
        # We don't pass overdraft_limit to parent because parent doesn't know about it
        super().__init__(name, account_number, account_type, phone_number, balance)
        
        # overdraft_limit is extra — only CurrentAccount has this
        # Example: if balance is 1000 and overdraft_limit is 500, user can withdraw up to 1500
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # This OVERRIDES the withdraw() method from BankAccount
        # BankAccount only checks balance, but CurrentAccount checks balance + overdraft_limit

        # Step 1: Amount must be greater than zero
        if amount <= 0:
            raise InvalidAmountError("Invalid Amount")

        # Step 2: Amount must not exceed balance + overdraft limit combined
        if amount > (self.balance + self.overdraft_limit):
            raise OverdraftError("Insufficient available funds for this transaction.")
        
        # Step 3: If both checks pass, deduct from balance
        else:
            self.balance -= amount
