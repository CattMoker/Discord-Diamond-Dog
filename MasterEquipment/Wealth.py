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