from MasterEquipment.Equipment import Equipment as Equipment


class Waterborne(Equipment):
    speed = None

    def __init__(self, inCategory, inCost, inWeight, inSpeed):
        self.speed = inSpeed
        super().__init__(inCategory, inCost, inWeight)

    def getSpeed(self):
        return self.speed

    def setSpeed(self, inSpeed):
        self.speed = inSpeed

    def toString(self):
        super().toString()
        print("Speed: " + self.getSpeed())

    def botMessage(self):
        return "Name: " + self.getCategory() + " Cost: " + self.getCost() + " Speed: " + self.getSpeed()