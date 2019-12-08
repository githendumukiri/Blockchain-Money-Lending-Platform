from pip._vendor.distlib.compat import raw_input
from project import User
from project import Transactions
#Helps set the username, and any other method helpers
class ExtraTools:
    def __init__(self):
            pass

    def getmakeaccountnumber(self,username):
        accountnum_set = []
        accountNum = ""
        for i in username:
            accountnum_set.append(str(ord(i)))

        return accountNum.join(accountnum_set)
#Main class where everything will be done.
class Main:
    done_session = False
    UseExtraTools = ExtraTools()

    print("Welcome to New Vision Banking")
    #Holds all the accounts

    Users = []
    addAccount = True
    #Takes in users per session on a while loop
    while addAccount:
        askSystem = raw_input("Add a user [Y/N]? ")
        if askSystem == "N":
                addAccount = False
        else:
            print("Perfect! Follow the instructions below")
            currentUser_firstname = raw_input("Enter a firstname: ")
            currentUser_lastname = raw_input("Enter a lastname: ")
            currentUser_passcode = raw_input("Enter a 10 character passcode: ")
            while len(currentUser_passcode) != 10:
                currentUser_passcode = raw_input("Please try again: ENTER A 10 CHARACTER PASSCODE: ")
            currentUser_investment = raw_input("Enter your initial deposit: ")
            currentUserName = currentUser_firstname + currentUser_lastname
            currentUser = User.User(UseExtraTools.getmakeaccountnumber(currentUserName),currentUser_passcode ,currentUser_investment)
            Users.append(currentUser)

    print("Current users in this session:")
    for x in range(0,Users.__len__()):
        print(str(x) + ": " + str(Users.__getitem__(x).get_account_number()))

    
    while done_session != True:
        print("Which user are you?")

        for i in Users:
            print(i)


