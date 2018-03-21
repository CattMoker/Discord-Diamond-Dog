from MasterEquipment.Equipment import Equipment as Equipment


class LifeExpenses(Equipment):
    price = None

    def _init_LifeExpenses(self, inName, inCost, inWeight, inPrice):
        super().__init__(inName, inCost, inWeight)

        self.price = inPrice

    def getPrice(self):
        return self.price

    def setPrice(self, inPrice):
        self.price = inPrice
