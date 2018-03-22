from MasterEquipment.Equipment import Equipment as Equipment


class DrawnVehicles(Equipment):
    name = ""

    def _init_DrawnVehicles(self, inCategory, inName, inCost, inWeight):
        super().__init__(inCategory, inCost, inWeight)

        self.name = inName

    def getName(self):
        return self.name

    def setName(self, inSubName):
        self.name = inSubName
