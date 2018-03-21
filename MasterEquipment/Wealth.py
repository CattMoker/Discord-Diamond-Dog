from MasterEquipment.Equipment import Equipment as Equipment


class Wealth(Equipment):
    funds = None

    def _init_Wealth(self, inName, inCost, inWeight, inFunds):
        super().__init__(inName, inCost, inWeight)

        self.funds = inFunds

    def getFunds(self):
        return self.funds

    def setFunds(self, inFunds):
        self.funds = inFunds
