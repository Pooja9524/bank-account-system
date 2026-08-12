# Bank Account Management System

A modular banking application built with Python, demonstrating object-oriented design, inheritance, custom exception handling, transaction management, and persistent data storage.

## Overview

The Bank Account Management System supports multiple account types and provides core banking operations such as deposits, withdrawals, loan payments, interest calculation, overdraft handling, and transaction tracking.

The project is structured into separate modules to keep business logic, utilities, and data storage organized and maintainable.

## Key Features

- Support for Savings, Current, and Loan Accounts
- Deposit and withdrawal operations
- Savings account interest calculation
- Current account overdraft support
- Loan payment management
- Custom exception handling for invalid transactions
- Transaction tracking using Pandas DataFrames
- Account data persistence using CSV
- Object-oriented and modular project structure

## Account Types

### Bank Account
Base class containing common account attributes and banking operations shared across account types.

### Savings Account
Extends `BankAccount` with an interest rate and functionality to calculate and add interest to the account balance.

### Current Account
Extends `BankAccount` with overdraft functionality, allowing withdrawals beyond the available balance within a defined overdraft limit.

### Loan Account
Extends `BankAccount` and manages outstanding loan amounts through payment functionality.

## Object-Oriented Programming

This project demonstrates several core OOP concepts:

- **Inheritance** — specialized account classes inherit common functionality from `BankAccount`.
- **Method Overriding** — `CurrentAccount` provides its own implementation of `withdraw()`.
- **Encapsulation** — account data and related operations are organized within classes.
- **`super()`** — child classes reuse the initialization logic of the parent class.
- **Polymorphism** — different account types can provide specialized behavior while sharing a common interface.

## Exception Handling

Custom exceptions are implemented to handle invalid banking operations:

- `InsufficientFundsError`
- `OverdraftError`
- `InvalidAmountError`

This provides clear and meaningful error handling for different transaction scenarios.

## Transaction Management

The `TransactionManager` uses Pandas to maintain transaction records, including:

- Account number
- Account holder
- Transaction type
- Transaction amount
- Date and time
- Balance after the transaction

Transactions can be filtered by account number for account-specific transaction history.

## Data Persistence

Account information is maintained in a CSV file located in the `Data` directory.

```text
Data/accounts.csv
