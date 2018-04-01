from MasterEquipment.Equipment import Equipment as Equipment


class Services(Equipment):
    name = ""
    pay = ""

    def __init__(self, inCategory, inName, inCost, inWeight, inPay):
        super().__init__(inCategory, inCost, inWeight)

        self.name = inName
        self.pay = inPay

    def getName(self):
        return self.name

    def getPay(self):
        return self.pay

    def setName(self, inName):
        self.name = inName

    def setPay(self, inPay):
        self.pay = inPay

    def toString(self):
        super().toString()
        print("Name: " + self.getName() + " Pay: " + self.getPay())

    def botMessage(self):
        return "Category: " + self.getCategory() + " Name: " + self.getName() + " Pay: " + self.getPay()