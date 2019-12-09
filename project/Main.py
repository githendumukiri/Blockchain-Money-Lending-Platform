from project import Account
from project import SendingAccount
from project import ReceivingAccount
from project import Transactions
from project import Blockchain
from project.Blockchain import Block


class Main:

    # keep track of all the accounts
    accounts = []
    print("Welcome to Wenmo")

    # User 1 prompts
    user1_username = input("Enter a username: ")
    user1_investment = input("Enter your initial deposit: ")
    user1 = Account.Account(user1_username, user1_investment)
    accounts.append(user1)

    # User 2 prompts
    print("Hello User 2! Let's get started, please follow the instructions bellow - ")
    user2_username = input("Enter a username: ")
    user2_investment = input("Enter your initial deposit: ")
    user2 = Account.Account(user2_username, user2_investment)
    accounts.append(user2)

    # Finding the sending user from array of users, we could use hashtable for O(1) lookup speed
    sending_user = None
    unknown_user = input("Please enter your username: ")
    for i in accounts:
        if unknown_user == i.get_username():
            # defining unknown user's attributes
            sending_user = SendingAccount.SendingAccount(i.get_balance())
            sending_user.set_username(i.get_username())
    # Initiating transaction
    amount = input("How much money where you looking to send?: ")
    # Finding the receiving user from array of users, we could use hashtable for O(1) lookup speed
    unknown_user = input("To whom are you sending the money to?: ")
    receiving_user = None
    for i in accounts:
        if unknown_user == i.get_username():
            receiving_user = ReceivingAccount.ReceivingAccount(i.get_balance())
            receiving_user.set_username(i.get_username())
    # Completing the transaction, crediting the receiving account & debiting the sending account
    sending_user.debit(amount)
    receiving_user.credit(amount)
    # Create a transaction object, passing the users/accounts as args
    transaction = Transactions.Transaction(sending_user, receiving_user)
    # Creating the BlockChain
    blockchain = Blockchain.Blockchain()
    # Mining a block passing the transaction detail to the data field
    blockchain.mine(Block(transaction.transaction_detail()))
