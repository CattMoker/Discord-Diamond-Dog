from MasterEquipment.Equipment import Equipment as Equipment


class LifeExpenses(Equipment):
    price = None

    def __init__(self, inCategory, inCost, inWeight, inPrice):
        super().__init__(inCategory, inCost, inWeight)

        self.price = inPrice

    def getPrice(self):
        return self.price

    def setPrice(self, inPrice):
        self.price = inPrice

    def toString(self):
        super().toString()
        print("Price: " + self.getPrice())

    def botMessage(self):
        return super().botMessage() + "Price: " + self.getPrice()