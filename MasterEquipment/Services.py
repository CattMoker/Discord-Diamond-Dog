from MasterEquipment.Equipment import Equipment as Equipment


class Services(Equipment):
    subName = ""
    pay = ""

    def _init_Services(self, inName, inSubName, inCost, inWeight, inPay):
        super().__init__(inName, inCost, inWeight)

        self.subName = inSubName
        self.pay = inPay

    def getSubName(self):
        return self.subName

    def getPay(self):
        return self.pay

    def setSubName(self, inSubName):
        self.subName = inSubName

    def setPay(self, inPay):
        self.pay = inPay
