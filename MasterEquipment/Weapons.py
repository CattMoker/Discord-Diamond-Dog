from MasterEquipment.Equipment import Equipment as Equipment


class Weapons(Equipment):
    subName = ""

    weaponType = None
    damage = None
    properties = None

    def _init_Weapons(self):
        subName = ""

        weaponType = ""
        damage = ""
        properties = ""

    def _init_Weapons(self, inName, inSubName, inCost, inWeight, inWeaponType, inDamage, inProperties):
        super().__init__(inName, inCost, inWeight)
        self.subName = inSubName

        self.weaponType = inWeaponType
        self.damage = inDamage
        self.properties = inProperties

    def getSubName(self):
        return self.subName

    def getWeaponType(self):
        return self.weaponType

    def getDamage(self):
        return self.damage

    def getProperties(self):
        return self.properties

    def setSubName(self, inSubName):
        self.subName = inSubName

    def setWeaponType(self, inWeaponType):
        self.weaponType = inWeaponType

    def setDamage(self, inDamage):
        self.damage = inDamage

    def setProperties(self, inProperties):
        self.properties = inProperties
