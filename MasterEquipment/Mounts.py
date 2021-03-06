from MasterEquipment.Equipment import Equipment as Equipment


class Mounts(Equipment):
    speed = None
    carryingCapacity = None

    def __init__(self, inCategory, inCost, inWeight, inSpeed, inCarryingCapacity):
        super().__init__(inCategory, inCost, inWeight)

        self.speed = inSpeed
        self.carryingCapacity = inCarryingCapacity

    def getSpeed(self):
        return self.speed

    def getCarryingCapacity(self):
        return self.carryingCapacity

    def setSpeed(self, inSpeed):
        self.speed = inSpeed

    def setCarryingCapacity(self, inCarryingCapacity):
        self.carryingCapacity = inCarryingCapacity

    def toString(self):
        super().toString()
        print("Speed: " + self.getSpeed() + " Carrying Capacity: " + self.getCarryingCapacity())

    def botMessage(self):
        return "Name: " + self.getCategory() + " Cost: " + self.getCost() + " Speed: " + self.getSpeed() + " Carrying Capacity: " + self.getCarryingCapacity()