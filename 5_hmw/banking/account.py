from transaction import Transaction
from timezone import TimeZone
from datetime import datetime


class Account:
    _account_number = 0
    interest_rate = 0.5

    def __init__(self, first, last, tz):
        self.first_name = first
        self.last_name = last
        self.tz = tz
        self._balance = 0
        self.account_id = Account._account_number
        Account._account_number += 1

    def deposit(self, amount):
        if amount <= 0:
            transaction = Transaction(self.account_id, 'X', TimeZone.timezone_offsets[self.tz])
            return transaction

        self._balance += amount
        transaction = Transaction(self.account_id, 'D', TimeZone.timezone_offsets[self.tz])
        return transaction

    def withdraw(self, amount):
        if amount > self._balance:
            transaction = Transaction(self.account_id, 'X', TimeZone.timezone_offsets[self.tz])
            return transaction

        self._balance -= amount
        transaction = Transaction(self.account_id, 'D', TimeZone.timezone_offsets[self.tz])
        return transaction

    def deposit_rate(self):
        self._balance += self._balance * Account.interest_rate
        transaction = Transaction(self.account_id, 'I', TimeZone.timezone_offsets[self.tz])
        return transaction

    @property
    def balance(self):
        return self._balance
