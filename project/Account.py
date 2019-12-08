class Account:
    # initialize the account class with field variables: username, deposit

    accountCount = 0
    setAccount = []
    def __init__(self, account_number,passcode ,deposit):
        # set balance equal to initial deposit
        self._balance = deposit
        self._account_number = account_number
        self.passcode = passcode
        Account.accountCount += 1
        Account.setAccount.append(self)

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_account_number(self):
        return self._account_number

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

