from project.ReceivingAccount import ReceivingAccount
from project.SendingAccount import SendingAccount
from project import Blockchain
from project import User
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
    @property
    def transaction_detail(self):
        self._transaction_complete = True
        return ("Sending Account Number: " + str(SendingAccount.get_account_number(self)) +
                " Sending Account Debit: " + str(SendingAccount.get_debit_amount(self)) +
                " Sending Account Balance: " + str(SendingAccount.get_balance(self)) +
                " Receiving Account Number: " + str(ReceivingAccount.get_account_number(self)) +
                " Receiving Account Credit: " + str(ReceivingAccount.get_credit_amount(self)) +
                " Receiving Account Balance: " + str(ReceivingAccount.get_balance(self)))

class TransactionChain(Blockchain):
    def __init__(self):
        Blockchain.Blockchain.__init__()

    @staticmethod
    def addTransaction(transactionID):
            blockChainLen = Blockchain.Blockchain.blockChainLen()
            Blockchain.Blockchain.mine(transactionID)
            if blockChainLen < (blockChainLen +1):
                return True
            else:
                return False


    def sendmoney_ac1_ac2(self,User1,User2,exchange):
            transactionID = Blockchain.Block(exchange)
            if self.addTransaction(exchange):
                User1.debit(exchange)
                User2.credit(exchange)
            else:
                print("Error In Transaction, try again!")