from MasterEquipment.Equipment import Equipment as Equipment


class Weapons(Equipment):
    name = ""

    weaponType = None
    damage = None
    properties = None

    def _init_Weapons(self):
        subName = ""

        weaponType = ""
        damage = ""
        properties = ""

    def _init_Weapons(self, inCategory, inName, inCost, inWeight, inDamage, inProperties):
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
