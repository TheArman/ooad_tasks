from timezone import TimeZone
from datetime import datetime, timedelta


class Transaction:
    _transaction_id = 0

    def __init__(self, account_id, code, acc_time):
        self.account_id = account_id
        self.code = code
        self.time_utc = datetime.now()
        time_difference = timedelta(hours=acc_time)
        self.time = self.time_utc + time_difference
        self.id = Transaction._transaction_id
        Transaction._transaction_id += 1

    def __repr__(self):
        return f'{self.code}-{self.account_id}-{self.time_utc}-{self.id}'
