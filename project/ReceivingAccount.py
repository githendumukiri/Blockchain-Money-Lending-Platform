from project.Account import Account


class ReceivingAccount(Account):

    def __init__(self, balance):
        self._balance = balance
        self._credit_amount = 0
        self.funds_received = False

    def credit(self, amount):
        self._credit_amount = amount
        self._balance += amount
        self.funds_received = True

    def get_credit_amount(self):
        return self._credit_amount
