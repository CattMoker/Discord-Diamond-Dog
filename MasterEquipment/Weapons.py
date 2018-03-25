from MasterEquipment.Equipment import Equipment as Equipment


class Weapons(Equipment):
    name = ""

    damage = None
    properties = None

    def __init__(self):
        subName = ""

        weaponType = ""
        damage = ""
        properties = ""

    def __init__(self, inCategory, inName, inCost, inWeight, inDamage, inProperties):
        super().__init__(inCategory, inCost, inWeight)
        self.name = inName

        self.damage = inDamage
        self.properties = inProperties

    def getName(self):
        return self.name

    def getWeaponType(self):
        return self.weaponType

    def getDamage(self):
        return self.damage

    def getProperties(self):
        return self.properties

    def setName(self, inName):
        self.name = inName

    def setDamage(self, inDamage):
        self.damage = inDamage

    def setProperties(self, inProperties):
        self.properties = inProperties

    def toStrings(self):
        super().toString()
        print("Name: " + self.getName() + " Weapon Type: " + self.getWeaponType() + " Damage: " + self.getDamage() + " Properties: " + self.getProperties())