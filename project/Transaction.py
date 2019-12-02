from project.ReceivingAccount import ReceivingAccount
from project.SendingAccount import SendingAccount


class Transaction(SendingAccount, ReceivingAccount):

    def __init__(self):
        self._transaction_complete = False

    def get_transaction_detail(self):

        print("Sending Account Number: " + str(SendingAccount.get_account_number(self)))
        print("Sending Account Debit: " + str(SendingAccount.get_debit_amount(self)))
        print("Sending Account Balance: " + str(SendingAccount.get_balance(self)))

        print("Receiving Account Number: " + str(ReceivingAccount.get_account_number(self)))
        print("Receiving Account Credit: " + str(ReceivingAccount.get_credit_amount(self)))
        print("Receiving Account Balance: " + str(ReceivingAccount.get_balance(self)))

    # data for the block-chain
    def transaction_detail(self):
        self._transaction_complete = True
        return ("Sending Account Number: " + str(SendingAccount.get_account_number(self)) +
                " Sending Account Debit: " + str(SendingAccount.get_debit_amount(self)) +
                " Sending Account Balance: " + str(SendingAccount.get_balance(self)) +
                " Receiving Account Number: " + str(ReceivingAccount.get_account_number(self)) +
                " Receiving Account Credit: " + str(ReceivingAccount.get_credit_amount(self)) +
                " Receiving Account Balance: " + str(ReceivingAccount.get_balance(self)))
