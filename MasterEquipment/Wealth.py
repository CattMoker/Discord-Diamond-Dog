from MasterEquipment.Equipment import Equipment as Equipment


class Wealth(Equipment):
    funds = None

    def __init__(self, inCategory, inCost, inWeight, inFunds):
        super().__init__(inCategory, inCost, inWeight)

        self.funds = inFunds

    def getFunds(self):
        return self.funds

    def setFunds(self, inFunds):
        self.funds = inFunds

    def toString(self):
        super().toString()
        print("Funds: " + self.getFunds())

    def botMessage(self):
        return super().botMessage() + "Funds: " + self.getFunds()