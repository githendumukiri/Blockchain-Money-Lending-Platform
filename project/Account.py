from random import randint


class AccountProfile:

        numberOfAccounts = 0

        def __init__(self,firstname,lastname,balance):
                self.firstname = firstname
                self.lastname = lastname
                self.balance = balance
                self.accountNumber = randint(0, 10) + randint(randint(30, 40), randint(500, 1000)) + AccountProfile.numberOfAccounts
                AccountProfile.numberOfAccounts+=1


        def getUsername(self):
                firstname_cut = self.firstname[0:1]
                return firstname_cut + self.lastname



        def getBalance(self):
                return  self.balance

        def setBalance(self,new_investment):
                self.investment = new_investment

        def TransactionTag(self,new_transcationID):
                tag = "000" + self.accountNumber.__str__() + "0" +  new_transcationID.__str__()
                return tag




