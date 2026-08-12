import pandas as pd
from datetime import datetime


class TransactionManager():

    def __init__(self):
        # Creates an empty DataFrame to store all transactions
        # Each transaction will contain account number, holder, type, amount,
        # date/time, and balance after the transaction
        self.transactions = pd.DataFrame(
            columns=[
                "account_number",
                "account_holder",
                "transaction_type",
                "amount",
                "date_time",
                "balance_after"
            ]
        )

    def add_transaction(
        self,
        account_number,
        account_holder,
        transaction_type,
        amount,
        balance_after
    ):
        # Gets the current date and time when the transaction happens
        date_time = datetime.now()

        # Creates a new transaction as a dictionary inside a list
        new_row = [{
            "account_number": account_number,
            "account_holder": account_holder,
            "transaction_type": transaction_type,
            "amount": amount,
            "date_time": date_time,
            "balance_after": balance_after
        }]

        # Converts the new transaction into a DataFrame
        # and adds it to the existing transactions DataFrame
        # ignore_index=True creates a new correct index
        self.transactions = pd.concat(
            [self.transactions, pd.DataFrame(new_row)],
            ignore_index=True
        )

    def get_transactions(self, account_number):
        # Returns only the transactions belonging to the given account number
        return self.transactions[
            self.transactions["account_number"] == account_number
        ]
