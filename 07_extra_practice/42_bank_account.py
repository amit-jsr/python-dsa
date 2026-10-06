"""Problem 42

OOP design: write a `BankAccount` class with `deposit`, `withdraw` and
`get_balance`. Reject negative amounts, prevent overdrawing with a clear
error, and keep a transaction history. Add a `__repr__` for readable printing.

Example:
Input:  acct = BankAccount(); acct.deposit(100); acct.withdraw(30); acct.get_balance()
Output: 70

Input:  acct.withdraw(500)
Output: raises an error: insufficient funds

Input:  acct.deposit(-5)
Output: raises an error: amount must be positive
"""


# Write your solution below

class BankAccount:
    def __init__(self):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass

    def __repr__(self):
        pass
