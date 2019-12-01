class AccountProfile:

        def __init__(self):
                self.firstname = "temp"

        def __init__(self,firstname,lastname,investment):
                self.firstname = firstname
                self.lastname = lastname
                self.investment = investment

        def getUsername(self):
                firstname_cut = self.firstname[0:1]
                return firstname_cut + self.lastname



        def getInvestment(self):
                return  self.investment

        def setInvestment(self,new_investment):
                self.investment = new_investment


accnt1= AccountProfile("Emmanuel","Chalumeau",3000)

print(accnt1.getUsername())
print(accnt1.getInvestment())
accnt1.setInvestment(400)
print(accnt1.getInvestment())

