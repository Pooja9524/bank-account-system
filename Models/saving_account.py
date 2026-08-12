# SavingsAccount INHERITS from BankAccount
# Key difference: has an interest_rate that can be applied to grow the balance

from Models.bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, account_number, account_type, phone_number, interest_rate, balance=0):

        # super() passes common details to BankAccount's __init__
        # interest_rate is NOT passed to parent — it is unique to SavingsAccount
        super().__init__(name, account_number, account_type, phone_number, balance)

        # interest_rate is the percentage used to calculate monthly/yearly interest
        self.interest_rate = interest_rate

    def add_interest(self):
        # Calculates interest amount using: balance × interest_rate / 100
        # Then reuses the parent's deposit() method to add interest to balance
        # This avoids rewriting deposit logic — a key benefit of inheritance
        balance = (self.balance * self.interest_rate) / 100
        self.deposit(balance)
