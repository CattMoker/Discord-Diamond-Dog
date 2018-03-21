from MasterEquipment.Equipment import Equipment as Equipment

class Armor(Equipment):
    subName = None
    armorClass = None
    strength = None
    stealth = None

    def __init__(self, inName, inSubName, inCost, inWeight, inArmorClass, inStrength, inStealth):
        super().__init__(inName, inCost, inWeight)

        self.armorClass = inArmorClass
        self.strength = inStrength
        self.stealth = inStealth
        self.subName = inSubName

    def getSubName(self):
        return self.subName

    def getArmorClass(self):
        return self.armorClass

    def getStrength(self):
        return self.strength

    def getStealth(self):
        return self.stealth

    def setArmorClass(self, inArmorClass):
        self.armorClass = inArmorClass

    def setStrength(self, inStrength):
        self.strength = inStrength

    def setStealth(self, inStealth):
        self.stealth = inStealth
