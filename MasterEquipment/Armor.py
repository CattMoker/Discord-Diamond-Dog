from MasterEquipment.Equipment import Equipment as Equipment

class Armor(Equipment):
    name = None
    armorClass = None
    strength = None
    stealth = None

    def __init__(self, inCategory, inName, inCost, inWeight, inArmorClass, inStrength, inStealth):
        super().__init__(inCategory, inCost, inWeight)

        self.armorClass = inArmorClass
        self.strength = inStrength
        self.stealth = inStealth
        self.name = inName

    def getSubName(self):
        return self.name

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
