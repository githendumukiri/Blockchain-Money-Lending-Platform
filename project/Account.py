class Account:
    # initialize the account class with field variables: username, deposit
    def __init__(self, username, deposit):
        # set balance equal to initial deposit
        self._balance = deposit
        self._username = username

    def set_username(self, username):
        self._username = username

    def get_username(self):
        return self._username

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

