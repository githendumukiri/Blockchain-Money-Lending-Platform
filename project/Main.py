from project import User
from project import Transactions

class Main:

    # keep track of all the accounts
    accounts = []
    print("Welcome to New Age Banking")

    # User 1 prompts
    print("Hello User 1! Let's get started, please follow the instructions bellow - ")
    user1_username = input("Enter a username: ")
    user1_investment = input("Enter your initial deposit: [only enter NUMBERS] ")
    user1 = User.User(user1_username,int(user1_investment))
    accounts.append(user1)

    # User 2 prompts
    print("Hello User 2! Let's get started, please follow the instructions bellow - ")
    user2_username = input("Enter a username: ")
    user2_investment = input("Enter your initial deposit: [only enter NUMBERS] ")
    user2 = User.User(user2_username,int(user2_investment))
    accounts.append(user2)
    #False: if session is active True: session inactive
    session_satus = False

    # Creating the BlockChain
    transactionChain = Transactions.TransactionChain()

    while session_satus == False:
        # Finding the sending user from array of users, we could use hashtable for O(1) lookup speed
        #sending_user = None

        chosen_user = input("Please enter your username: ")
        for i in accounts:
            if chosen_user == i.getaccountname():
                    selectednumber = i.getlinenumber()

        chosen_dst = input("Who are you working with? ")
        if chosen_user != chosen_dst:
            for i in accounts:
                if chosen_dst == i.getaccountname():
                    selecteddstnumber = i.getlinenumber()

        transactionselection = input("What would you like to do? Send[0] Request[1] ")
        #Chose to send money
        if transactionselection == "0":
            send_amount = input("How much do you want to send? [only enter NUMBERS] ")
            #Checks if input is a number
            if int(send_amount):
                # Checks account balance
                if accounts[selectednumber].checkBalance(send_amount) == 1:
                    #Creates Transaction ID
                    current_transactionid = str(accounts[selectednumber].getaccountname()) + str(send_amount) + str(accounts[selecteddstnumber].getaccountname())
                    #Creates Transaction Block
                    print(current_transactionid)
                    transaction = Transactions.Transaction(str(current_transactionid))
                    print("Approval pending...")
                    #adds Block to Chain
                    transactionChain.mine(transaction)
                    #Checks if it has been added
                    if transaction.getapproval() == 1:
                        print("Transaction as been approved!")
                        #Sends money
                        accounts[selecteddstnumber].receivemoney(accounts[selectednumber].sendmoney(send_amount))
                        #Update on the balances
                        for i in accounts:
                            print(str(i.getaccountname()) + ": Balance = " + str(i.getbalance()))
                    else:
                        print("Your transaction was not approved!")
                else:
                    print("Not enough money in your account!")

        #Chose to request money
        elif transactionselection == "1":
            request_amount = input("How much do you want to request ")
            #Checks if input is a number
            if int(request_amount):
                #Checks for approval of other User
                dst_approval = input(accounts[selecteddstnumber].getaccountname()+", Do you agree? [Y/N]")
                #Clears Approvals
                if dst_approval == "Y":
                    #Checks account balance
                    if accounts[selecteddstnumber].checkBalance(request_amount) == 1:
                        #Creates Transaction ID
                        current_transactionid = str(accounts[selectednumber].getaccountname()) + str(request_amount) + str(accounts[selecteddstnumber].getaccountname())
                        #Creates Transaction Block
                        transaction = Transactions.Transaction(str(current_transactionid))
                        print("Approval pending...")
                        #Adds to Chain
                        transactionChain.mine(transaction)
                        #Checks if it has been added
                        if transaction.getapproval() == 1:
                            print("Transaction as been approved!")
                            #Sends money
                            accounts[selectednumber].receivemoney(accounts[selecteddstnumber].sendmoney(request_amount))
                            #Checks balances
                            for i in accounts:
                                print(str(i.getaccountname()) + ": Balance = " + str(i.getbalance()))
                        else:
                            print("Your transaction was not approved!")
                    else:
                        print("Not enough money in your account!")
                else:
                    print("Your transaction was not approved!")

        #Allows the program to continue or stop
        status = input("Is that all for this session? [Y/N] ")
        if status == "Y":
            session_satus = True
            print("Thank you for working with New Age Banking, come back soon!")
            print("---------------------------------------")
            print("Here are your chains:")
            #Runs through/displays Sending Chain
            print("Transaction Chain: ")
            while transactionChain.head != None:
                print(transactionChain.head)
                transactionChain.head = transactionChain.head.next
            #Runs through/displays Request Chain
            SystemExit

        else:
            session_satus = False
