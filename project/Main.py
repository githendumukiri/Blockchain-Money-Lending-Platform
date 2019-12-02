from pip._vendor.distlib.compat import raw_input

from project import Account

class Main:

        #need to setup while loops for the exit and return
        print("Welcome to Wenmo")
        print("Hello User  1! Let's get started, please follow the instructions bellow - ")

        user1_firstname = raw_input("Enter a firstname:")
        user1_lastname = raw_input("Enter a lastname:")
        user1_investment = raw_input("Investment:")

        user1 = Account.Account(user1_firstname)
        print(user1.getUsername())

        print("Hello User 2! Let's get started, please follow the instructions bellow - ")
        user2_firstname = raw_input("Enter a firstname:")
        user2_lastname = raw_input("Enter a lastname:")
        user2_investment = raw_input("Investment:")

        user2 = Account.AccountProfile(user2_firstname, user2_lastname, user2_investment)
        print(user2.getUsername())