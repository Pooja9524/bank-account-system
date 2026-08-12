# LoanAccount INHERITS from BankAccount
# Key difference: tracks a loan_amount that reduces with each payment
# Unlike other accounts, the goal here is to reduce loan_amount to zero

from Models.bank_account import BankAccount
from Utils.exceptions import InvalidAmountError

class LoanAccount(BankAccount):
    def __init__(self, name, account_number, account_type, phone_number, loan_amount, balance=0):

        # super() passes common details to BankAccount's __init__
        # loan_amount is NOT passed to parent — it is unique to LoanAccount
        super().__init__(name, account_number, account_type, phone_number, balance)

        # loan_amount is the total loan the customer needs to repay
        self.loan_amount = loan_amount

    def make_payment(self, payment):
        # Reduces loan_amount with each payment made by the customer

        # Step 1: Payment must be greater than zero
        if payment <= 0:
            raise InvalidAmountError("Invalid Amount")

        # Step 2: Payment cannot exceed remaining loan amount
        if payment > self.loan_amount:
            raise InvalidAmountError("Payment exceeds loan amount")

        # Step 3: Deduct payment from remaining loan
        else:
            self.loan_amount -= payment
