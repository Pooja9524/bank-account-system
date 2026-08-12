# Custom exception raised when withdrawal amount exceeds account balance
class InsufficientFundsError(Exception):
    def __init__(self,message):
        super().__init__(message)

# Custom exception raised when withdrawal exceeds overdraft limit in Current Account
class OverdraftError(Exception):
    def __init__(self,message):
        super().__init__(message)

# Custom exception raised when deposit or withdrawal amount is zero or negative
class InvalidAmountError(Exception):
    def __init__(self,message):
        super().__init__(message)


