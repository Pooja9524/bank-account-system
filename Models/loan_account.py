from Models.bank_account import BankAccount
from Utils.exceptions import InvalidAmountError
class LoanAccount(BankAccount):
    def __init__(self,name,account_number,account_type,phone_number,loan_amount,balance=0):
        super().__init__(name,account_number,account_type,phone_number,balance)
        self.loan_amount=loan_amount
    def make_payment(self,payment):
        if payment<=0:
            raise InvalidAmountError("Invalid Amount")
        if payment>self.loan_amount:
            raise InvalidAmountError("Payment exceeds loan amount")
        else:
            self.loan_amount-=payment
