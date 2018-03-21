from MasterEquipment.Equipment import Equipment as Equipment

class AdventuringGear(Equipment):
    subName = ""

    def _init_AdventuringGear(self, inName, inSubName, inCost, inWeight):
        super().__init__(inName, inCost, inWeight)

        self.subName = inSubName

    def getSubName(self):
        return self.subName

    def setSubName(self, inSubName):
        self.subName = inSubName