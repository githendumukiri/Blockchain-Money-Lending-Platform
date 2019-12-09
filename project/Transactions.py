class Transaction:

    def __init__(self, sending_account, receiving_account):
        self._sending_account = sending_account
        self._receiving_account = receiving_account
        self._transaction_complete = False

    def get_transaction_detail(self):

        print("Sending Account Number: " + str(self._sending_account.get_username()))
        print("Sending Account Debit: " + str(self._sending_account.get_debit_amount()))
        print("Sending Account Balance: " + str(self._sending_account.get_balance()))

        print("Receiving Account Number: " + str(self._receiving_account.get_username()))
        print("Receiving Account Credit: " + str(self._receiving_account.get_credit_amount()))
        print("Receiving Account Balance: " + str(self._receiving_account.get_balance()))

    # data for the block-chain
    def transaction_detail(self):
        self._transaction_complete = True
        return ("Sending Account Number: " + str(self._sending_account.get_username()) +
                " Sending Account Debit: " + str(self._sending_account.get_debit_amount()) +
                " Sending Account Balance: " + str(self._sending_account.get_balance()) +
                " Receiving Account Number: " + str(self._receiving_account.get_username()) +
                " Receiving Account Credit: " + str(self._receiving_account.get_credit_amount()) +
                " Receiving Account Balance: " + str(self._receiving_account.get_balance()))

