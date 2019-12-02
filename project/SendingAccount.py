from project.Account import Account


class SendingAccount(Account):

    def __init__(self, balance):
        self._balance = balance
        self._debit_amount = 0

    def debit(self, amount):
        self._debit_amount = amount
        self._balance -= amount

    def get_debit_amount(self):
        return self._debit_amount
