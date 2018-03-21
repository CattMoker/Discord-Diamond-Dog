from MasterEquipment.Equipment import Equipment as Equipment


class Tools(Equipment):
    subName = ""

    def _init_Tools(self, inName, inSubName, inCost, inWeight):
        super().__init__(inName, inCost, inWeight)

        self.subName = inSubName

    def getSubName(self):
        return self.subName

    def setSubName(self, inSubName):
        self.subName = inSubName
