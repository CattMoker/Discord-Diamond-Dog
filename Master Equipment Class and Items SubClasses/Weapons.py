class Weapons(Equipment):
    weaponType = None
    damage = None
    properties = None
    name = None


    def _init_Weapons(self):
        weaponType = ""
        damage = ""
        properties = ""
        name = ""

    def _init_Weapons(self, inName, inWeaponType, inDamage, inProperties)
        Equipment._init_(inName, subName, cost, weight)

        self.name = inName
        self.weaponType = inWeaponType
        self.damage = inDamage
        self.properties = inProperties

    def setWeaponsCharacteristics(self, inName, inWeaponType, inDamage, inProperties)
        self.setName(inName)
        self.setWeaponType(inWeaponType)
        self.setDamage(inDamage)
        self.setProperties(inProperties)

    def getWeaponCharacteristics(self)
        print ("Name: " + self.getName())
        print ("Weapon Type: " + self.getWeaponType())
        print ("Damage: " + self.getDamage())
        print ("Properties: " + self.getProperties())

    def getName(self)
        self.name = inName
    def getWeaponType(self)
        self.weaponType = inWeaponType
    def getDamage(self)
        self.damage = inDamage
    def getProperties(self)
        self.properties = inProperties

    
    def setName(self, inName)
        self.name = inName
    def setWeaponType(self, inWeaponType)
        self.weaponType = inWeaponType
    def setDamage(self, inDamage)
        self.damage = inDamage
    def setProperties(self, inProperties)
        self.properties = inProperties


    def toString(self)
        self.getWeaponCharacteristics()