from pip._vendor.distlib.compat import raw_input

from project import Account



class Main():
    accounts = []
    print("Welcome to Wenmo")

    user1_firstname = raw_input("Enter a firstname: ")
    user1_lastname = raw_input("Enter a lastname: ")
    user1_investment = raw_input("Enter your initial deposit: ")

    user1 = Account.Account(user1_firstname, user1_lastname,user1_investment)
    accounts.append(user1)
    print("Hello User 2! Let's get started, please follow the instructions bellow - ")
    user2_firstname = raw_input("Enter a firstname: ")
    user2_lastname = raw_input("Enter a lastname: ")
    user2_investment = raw_input("Enter your initial deposit: ")

    user2 = Account.Account(user2_firstname,user1_lastname, user2_investment)
    accounts.append(user2)

    for x in range(0,accounts.__len__()):
        print(accounts.__getitem__(x).makeusername())

