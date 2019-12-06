from pip._vendor.distlib.compat import raw_input

from project import Account



class Main(object):


    def makeusername(self,first_name,last_name):
        return first_name[0,1] + last_name



    print("Welcome to Wenmo")

    user1_firstname = raw_input("Enter a firstname: ")
    user1_lastname = raw_input("Enter a lastname: ")

    user1_username = makeusername(user1_firstname, user1_lastname)

    user1_investment = raw_input("Enter your initial deposit:")

    user1 = Account.Account(user1_username, user1_investment)

    print("Hello User 2! Let's get started, please follow the instructions bellow - ")
    user2_firstname = raw_input("Enter a firstname:")
    user2_lastname = raw_input("Enter a lastname:")
    user2_investment = raw_input("Enter your initial deposit:")

    user2 = Account.Account(user2_firstname, user2_investment)
