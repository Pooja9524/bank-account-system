import pandas as pd
import os
from Models.saving_account import SavingsAccount
from Models.current_account import CurrentAccount
from Models.loan_account import LoanAccount
accounts={}
def generate_account_number():
    return 1001 + len(accounts)
def create_account():
    name=input("Enter Name:")
    phone_number=int(input("Enter the Phone Number:"))
    account_type=int(input("Account Types:\n1.Savings Account\n2.Current Account\n3.Loan Account\nEnter the Account Type:"))
    pin=int(input("Enter the PIN:"))
    account_number=generate_account_number()
    if(account_type==1):
        interest_rate = float(input("Enter interest rate: "))
        account=SavingsAccount(name,account_number,"Savings",phone_number,interest_rate)
    elif(account_type==2):
        overdraft_limit=int(input("Enter Overdraft Limit:"))
        account=CurrentAccount(name, account_number,"Current",phone_number,overdraft_limit)
    elif(account_type==3):
        loan_amount=int(input("Enter the Loan Amount:"))
        account=LoanAccount(name,account_number,"loan",phone_number,loan_amount)
    else:
        print("Invalid Account Type")
    accounts[account_number]={"account":account,"pin":pin}
    print(f"Account created successfully. Your account number is: {account_number}")
    save_accounts()  
def verify_account():
    acc_no=int(input("Enter the Account NUmber:"))
    pin_che=int(input("Enter the PIN:"))
    if (acc_no in accounts) and (accounts[acc_no]["pin"] == pin_che):
        return accounts[acc_no]["account"]
    else:
        print("Data does not Exist")
def deposit_money():
    account = verify_account()
    if account is not None:
        amount = float(input("Enter amount to deposit: "))
        try:
            account.deposit(amount)
            print("Deposit successful!")
            save_accounts() 
        except Exception as e:
            print(e)
def withdraw_money():
    account=verify_account()
    if account is not None:
        amount = float(input("Enter the Amount to be Withdraw:"))
        try:
            account.withdraw(amount)
            print("Amount Withdraw Successfully")
            save_accounts() 
        except Exception as e:
            print(e)
def check_balance():
    account=verify_account()
    if account is not None:
        print("Balance:",account)
def view_transaction():
    account=verify_account()
    if account is not None:
        result=account.transaction_manager.get_transactions(account.account_number)
        print(result)
def save_accounts():
    data = []
    for acc_no, details in accounts.items():
        account = details["account"]
        data.append({
            "account_number": acc_no,
            "name": account.name,
            "account_type": account.account_type,
            "phone_number": account.phone_number,
            "pin": details["pin"],
            "balance": account.balance
        })
    df = pd.DataFrame(data)
    df.to_csv("Data/accounts.csv", index=False)
def main():
    while True:
        print("Menu Option:")
        print("\t1.Create Account")
        print("\t2.Deposit")
        print("\t3.Withdraw")
        print("\t4.Check Balance")
        print("\t5.View Transaction")
        print("\t6.Exit")
        user=int(input("Choose a Banking Operation:"))
        if(user==1):
            create_account()
        elif(user==2):
            deposit_money()
        elif(user==3):
            withdraw_money()
        elif(user==4):
            check_balance()
        elif(user==5):
            view_transaction()
        elif(user==6):
            print("Session ended successfully")
            break
        else:
            print("Invalid Option")
if __name__ == "__main__":
    main()



