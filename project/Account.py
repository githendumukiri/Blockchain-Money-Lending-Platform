class Account:
    # initialize the account class with field variables: username, deposit
    def __init__(self, firstname,lastname, deposit):
        # set balance equal to initial deposit
        self._balance = deposit


    def set_account_number(self, account_number):
        self._account_number = account_number

    def makeusername(self):
        return self.firstname[0,1] + "_"+ self.lastname

    def get_account_number(self):
        return self._account_number

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

