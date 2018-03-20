class Armor(Equipment): 
    armorClass = None
    strength = None
    stealth = None
    name = None

    

    def _init_Armor(self):
        armorClass = ""
        strength = ""
        stealth = ""
        name = ""

   
    def _init_Armor(self, inName, inArmorClass, inStrength, inStealth)
        Equipment._init_(inName, subName, cost, weight)

        self.name = inName
        self.armorClass = inArmorClass
        self.strength = inStrength
        self.stealth = inStealth

    def setCharacteristics (self, inName, inArmorClass, inStrength, inStealth)
        self.setName(inName)
        self.setArmorClass(inArmorClass)
        self.setStrength(inStrength)
        self.setStealth(inStealth)

    def getCharacteristics (self)
        print ("Name: " + self.getName())
        print ("Armor Class: " + self.getArmorClass())
        print ("Strength: " + self.getStrength())
        print ("Stealth: " + self.getStealth())

    
    def getName(self)
        self.name = inName
    def getArmorClass(self)
        self.armorClass = inArmorClass
    def getStrength(self)
        self.strength = inStrength
    def getStealth(self)
        self.stealth = inStealth

    def setName (self, inName)
        self.name = inName
    def setArmorClass(self, inArmorClass)
        self.armorClass = inArmorClass
    def setStrength (self, inStrength)
        self.strength = inStrength
    def setStealth (self, inStealth)
        self.stealth = inStealth



    def toString(self)
        self.getCharacteristics()






    

