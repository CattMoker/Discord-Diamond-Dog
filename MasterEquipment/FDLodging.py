from MasterEquipment.Equipment import Equipment as Equipment


class FDLodging(Equipment):
    subName = ""

    def _init_FDLodging(self, inCategory, inName, inCost, inWeight):
        super().__init__(inCategory, inCost, inWeight)
        self.name = inName

    def getName(self):
        return self.subName

    def setName(self, inName):
        self.name = inName
