from MasterEquipment.Equipment import Equipment as Equipment

class FDLodging(Equipment):
    subName = ""

    def _init_FDLodging(self, inName, inSubName, inCost, inWeight):
        super().__init__(inName, inCost, inWeight)
        self.subName = inSubName

    def getSubName(self):
        return self.subName

    def setName(self, inSubName):
        self.subName = inSubName