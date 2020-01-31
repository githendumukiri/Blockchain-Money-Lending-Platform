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
    user1 = User.User(user1_username, int(user1_investment))
    accounts.append(user1)

    # User 2 prompts
    print("Hello User 2! Let's get started, please follow the instructions bellow - ")
    user2_username = input("Enter a username: ")
    user2_investment = input("Enter your initial deposit: [only enter NUMBERS] ")
    user2 = User.User(user2_username, int(user2_investment))
    accounts.append(user2)
    # False: if session is active True: session inactive
    session_status = False

    # Creating the BlockChain
    transactionChain = Transactions.TransactionChain()

    while not session_status:
        # Finding the sending user from array of users, we could use hashtable for O(1) lookup speed
        # sending_user = None

        chosen_user = input("Please enter your username: ")
        selected_number = 0
        selected_destination_number = 0
        for i in accounts:
            if chosen_user == i.get_username():
                selected_number = i.get_line_number()

        chosen_destination = input("Who are you working with? ")
        if chosen_user != chosen_destination:
            for i in accounts:
                if chosen_destination == i.get_username():
                    selected_destination_number = i.get_line_number()

        transaction_selection = input("What would you like to do? Send[0] Request[1] ")
        # Chose to send money
        if transaction_selection == "0":
            send_amount = input("How much do you want to send? [only enter NUMBERS] ")
            # Checks if input is a number
            if int(send_amount):
                # Checks account balance
                if accounts[selected_number].check_balance(send_amount) == 1:
                    # Creates Transaction ID
                    current_transaction_id = str(accounts[selected_number].get_username()) + str(send_amount) + str(
                        accounts[selected_destination_number].get_username())
                    # Creates Transaction Block
                    print(current_transaction_id)
                    transaction = Transactions.Transaction(str(current_transaction_id))
                    print("Approval pending...")
                    # adds Block to Chain
                    transactionChain.mine(transaction)
                    # Checks if it has been added
                    if transaction.get_approval() == 1:
                        print("Transaction as been approved!")
                        # Sends money
                        accounts[selected_destination_number].receive_money(accounts[selected_number].send_money(send_amount))
                        # Update on the balances
                        for i in accounts:
                            print(str(i.get_username()) + ": Balance = " + str(i.get_balance()))
                    else:
                        print("Your transaction was not approved!")
                else:
                    print("Not enough money in your account!")

        # Chose to request money
        elif transaction_selection == "1":
            request_amount = input("How much do you want to request ")
            # Checks if input is a number
            if int(request_amount):
                # Checks for approval of other User
                dst_approval = input(accounts[selected_destination_number].get_username() + ", Do you agree? [Y/N]")
                # Clears Approvals
                if dst_approval == "Y":
                    # Checks account balance
                    if accounts[selected_destination_number].check_balance(request_amount) == 1:
                        # Creates Transaction ID
                        current_transaction_id = str(accounts[selected_number].get_username()) + str(
                            request_amount) + str(accounts[selected_destination_number].get_username())
                        # Creates Transaction Block
                        transaction = Transactions.Transaction(str(current_transaction_id))
                        print("Approval pending...")
                        # Adds to Chain
                        transactionChain.mine(transaction)
                        # Checks if it has been added
                        if transaction.get_approval() == 1:
                            print("Transaction as been approved!")
                            # Sends money
                            accounts[selected_number].receive_money(accounts[selected_destination_number].send_money(request_amount))
                            # Checks balances
                            for i in accounts:
                                print(str(i.get_username()) + ": Balance = " + str(i.get_balance()))
                        else:
                            print("Your transaction was not approved!")
                    else:
                        print("Not enough money in your account!")
                else:
                    print("Your transaction was not approved!")

        # Allows the program to continue or stop
        status = input("Is that all for this session? [Y/N] ")
        if status == "Y":
            session_status = True
            print("Thank you for working with New Age Banking, come back soon!")
            print("---------------------------------------")
            print("Here are your chains:")
            # Runs through/displays Sending Chain
            print("Transaction Chain: ")
            while transactionChain.head is not None:
                print(transactionChain.head)
                transactionChain.head = transactionChain.head.next
            # Runs through/displays Request Chain
        else:
            session_status = False
