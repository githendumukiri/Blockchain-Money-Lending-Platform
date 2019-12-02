class AccountProfile:
    #initialize the account class
    def __init__(self, username):
        self._account_number = 0
        self._balance = 0

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_account_number(self):
        return self._account_number

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance
