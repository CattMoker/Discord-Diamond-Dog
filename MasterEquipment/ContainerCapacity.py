from MasterEquipment.Equipment import Equipment as Equipment

class ContainerCapacity(Equipment):
    subName = ""
    capacity = None

    def _init_ContainerCapacity(self, inName, inSubName, inCost, inWeight, inCapacity):
        super().__init__(inName, inCost, inWeight)
        self.subName = inSubName

        self.capacity = inCapacity

    def getSubName(self):
        return self.subName
    def getCapacity(self):
        return self.capacity

    def setSubName(self, inSubName):
        self.subName = inSubName
    def setCapacity(self, inCapacity):
        self.capacity = inCapacity


    
