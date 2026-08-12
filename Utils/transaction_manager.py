import pandas as pd
from datetime import datetime
class TransactionManager():
    def __init__(self):
        self.transactions = pd.DataFrame(columns=["account_number","account_holder","transaction_type","amount","date_time","balance_after"])
    def add_transaction(self,account_number,account_holder,transaction_type,amount,balance_after):
        date_time=datetime.now()
        new_row=[{
            "account_number":account_number,
            "account_holder":account_holder,
            "transaction_type":transaction_type,
            "amount":amount,
            "date_time": date_time,
            "balance_after":balance_after
        }]
        self.transactions=pd.concat([self.transactions,pd.DataFrame(new_row)],ignore_index=True)
    def get_transactions(self,account_number):
        return self.transactions[self.transactions["account_number"]==account_number]
             
