from MasterEquipment.Equipment import Equipment as Equipment


class Armor(Equipment):
    name = ""
    armorClass = ""
    strength = ""
    stealth = ""

    def __init__(self, inCategory, inName, inCost, inWeight, inArmorClass, inStrength, inStealth):
        super().__init__(inCategory, inCost, inWeight)

        self.armorClass = inArmorClass
        self.strength = inStrength
        self.stealth = inStealth
        self.name = inName

    def getName(self):
        return self.name

    def getArmorClass(self):
        return self.armorClass

    def getStrength(self):
        return self.strength

    def getStealth(self):
        return self.stealth

    def setName(self, inName):
        self.name = inName

    def setArmorClass(self, inArmorClass):
        self.armorClass = inArmorClass

    def setStrength(self, inStrength):
        self.strength = inStrength

    def setStealth(self, inStealth):
        self.stealth = inStealth

    def toString(self):
        super().toString()
        print("Name: " + self.getName() + " Armor Class: " + self.getArmorClass() + " Strength: " + self.getStrength() + " Stealth: " + self.getStealth())

    def botMessage(self):
        return super().botMessage() + "Name: " + self.getName() + " Armor Class: " + self.getArmorClass() + " Strength: " + self.getStrength() + " Stealth: " + self.getStealth()