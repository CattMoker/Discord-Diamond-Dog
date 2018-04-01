from MasterEquipment.Equipment import Equipment as Equipment


class ContainerCapacity(Equipment):
    name = ""
    capacity = None

    def __init__(self, inCategory, inCost, inWeight, inCapacity):
        super().__init__(inCategory, inCost, inWeight)

        self.capacity = inCapacity

    def getCapacity(self):
        return self.capacity

    def setCapacity(self, inCapacity):
        self.capacity = inCapacity

    def toString(self):
        super().toString()
        print("Name: " + self.getName() + " Capacity: " + self.getCapacity())

    def botMessage(self):
        return "Name: " + self.getCategory() + " Capacity: " + self.getCapacity()
