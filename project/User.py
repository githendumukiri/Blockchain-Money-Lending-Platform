from project import ReceivingAccount, SendingAccount


class User(ReceivingAccount, SendingAccount):

    def __init__(self, username, passcode, starting_balance):
        self.username = username
        self.passcode = passcode
        self.balace = starting_balance
        ReceivingAccount.__init__(self, starting_balance)
        SendingAccount.__init__(self, starting_balance)

    def check_password(self, passcode):
        if passcode == self.passcode:
            print("Welcome! What would you like to do today!")
        else:
            print("You have entered the wrong code, please try again later")

