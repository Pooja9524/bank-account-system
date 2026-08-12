# BankAccount is the BASE CLASS for all account types
# SavingsAccount, CurrentAccount, and LoanAccount all inherit from this class

from Utils.exceptions import InvalidAmountError, InsufficientFundsError
from Utils.transaction_manager import TransactionManager

class BankAccount():
    def __init__(self, name, account_number, account_type, phone_number, balance=0):
        # Initialize all common attributes shared by every account type
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.phone_number = phone_number
        self.balance = balance  # Default is 0 — new accounts start with no money

        # Every account gets its own TransactionManager to record history
        self.transaction_manager = TransactionManager()

    def deposit(self, amount):
        # Raises InvalidAmountError if amount is zero or negative
        if amount <= 0:
            raise InvalidAmountError("Invalid Amount")
        else:
            self.balance += amount
        # Logs every deposit into the pandas DataFrame inside TransactionManager
        self.transaction_manager.add_transaction(
            self.account_number, self.name, "deposit", amount, self.balance
        )

    def withdraw(self, amount):
        # First validates amount, then checks if balance is sufficient
        # Note: This method is OVERRIDDEN in CurrentAccount to allow overdraft
        if amount <= 0:
            raise InvalidAmountError("Invalid Amount")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient Funds")
        else:
            self.balance -= amount
            # Only logs if withdrawal actually succeeds
            self.transaction_manager.add_transaction(
                self.account_number, self.name, "withdraw", amount, self.balance
            )

    def __str__(self):
        # Dunder method (Double UNDERscore) — called automatically when print(account) is used
        # Without this Python would print a memory address like <object at 0x...>
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Account Type: {self.account_type}\n"
            f"Phone Number: {self.phone_number}\n"
            f"Balance: {self.balance}"
        )
