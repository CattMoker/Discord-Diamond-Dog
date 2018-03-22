from MasterEquipment.Equipment import Equipment as Equipment


class ContainerCapacity(Equipment):
    name = ""
    capacity = None

    def _init_ContainerCapacity(self, inCategory, inName, inCost, inWeight, inCapacity):
        super().__init__(inCategory, inCost, inWeight)
        self.name = inName

        self.capacity = inCapacity

    def getName(self):
        return self.name

    def getCapacity(self):
        return self.capacity

    def setName(self, inName):
        self.name = inName

    def setCapacity(self, inCapacity):
        self.capacity = inCapacity
