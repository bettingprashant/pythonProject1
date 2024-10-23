# Custom Exception Own

class BalanceLowException(Exception):

    def __init__(self,message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("ENter the Withdraw amount"))
if withdraw > balance:
    raise BalanceLowException("Balance is low")
else:
    print("Remain Bal",(balance-withdraw))