from MasterEquipment.Equipment import Equipment as Equipment


class AdventuringGear(Equipment):
    name = ""

    def __init__(self, inCategory, inName, inCost, inWeight):
        super().__init__(inCategory, inCost, inWeight)

        self.name = inName

    def getName(self):
        return self.name

    def setName(self, inName):
        self.name = inName
