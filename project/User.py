from project import ReceivingAccount, SendingAccount

class User(ReceivingAccount,SendingAccount):

    def __init__(self, username,passcode,startingBalance):
        self.username = username
        self.passcode = passcode
        self.balace = startingBalance



    def checkPassCode(self, thispasscode):
            if thispasscode == self.passcode:
                print("Welcome! What would you like to do today!")
            else:
                print("You have entered the wrong code, please try again later")