class Character:
    # basic characteristics
    name = None
    race = None
    charClass = None
    alignment = None

    # numerical characteristics
    age = None
    height = None
    weight = None

    # color characteristics
    hairColor = None
    eyeColor = None
    skinColor = None

    # abstract characteristics
    background = None
    traits = None
    ideals = None
    flaws = None
    bonds = None
    proficiencies = None

    def Character(self):
        # basic characteristics
        name = ""
        race = ""
        charClass = ""
        alignment = ""

        # numerical characteristics
        age = ""
        height = ""
        weight = ""

        # color characteristics
        hairColor = ""
        eyeColor = ""
        skinColor = ""

        # abstract characteristics
        background = ""
        traits = ""
        ideals = ""
        flaws = ""
        bonds = ""
        proficiencies = ""

    def Character(self, inName, inRace, inCharClass, inAlignment, inAge, inHeight, inWeight, inHairColor, inEyeColor, inSkinColor, inBackground, inTraits, inIdeals, inFlaws, inBonds, inProficiencies):
        # basic characteristics
        self.name = inName
        self.race = inRace
        self.charClass = inCharClass
        self.alignment = inAlignment

        # numerical characteristics
        self.age = inAge
        self.height = inHeight
        self.weight = inWeight

        # color characteristics
        self.hairColor = inHairColor
        self.eyeColor = inEyeColor
        self.skinColor = inSkinColor

        # abstract characteristics
        self.background = inBackground
        self.traits = inTraits
        self.ideals = inIdeals
        self.flaws = inFlaws
        self.bonds = inBonds
        self.proficiencies = inProficiencies

    # Chunked Setters
    def setBaseChar(self, inName, inRace, inCharClass, inAlignment):
        self.setName(inName)
        self.setRace(inRace)
        self.setCharClass(inCharClass)
        self.setAlignment(inAlignment)

    def setNumericalChar(self, inAge, inHeight, inWeight):
        self.setAge(inAge)
        self.setHeight(inHeight)
        self.setWeight(inWeight)

    def setColorChar(self, inHairColor, inEyeColor, inSkinColor):
        self.setHairColor(inHairColor)
        self.setEyeColor(inEyeColor)
        self.setSkinColor(inSkinColor)

    def setAbstractChar(self, inBackground, inTraits, inIdeals, inFlaws, inBonds, inProficiencies):
        self.setBackground(inBackground)
        self.setTraits(inTraits)
        self.setIdeals(inIdeals)
        self.setFlaws(inFlaws)
        self.setBonds(inBonds)
        self.setProficiencies(inProficiencies)

    # Chunked Getters
    def getBasicChar(self):
        print("Name: " + self.getName())
        print("Race: " + self.getRace())
        print("Character Class: " + self.getCharClass())
        print("Character Alignment: " + self.getAlignment())

    def getNumericalChar(self):
        print("Age: " + self.getAge())
        print("Height: " + self.getHeight())
        print("Weight: " + self.getWeight())

    def getColorChar(self):
        print("Hair Color: " + self.getHairColor())
        print("Eye Color: " + self.getEyeColor())
        print("Skin Color: " + self.getSkinColor())

    def getAbstractChar(self):
        print("Background: " + self.getBackground())
        print("Traits: " + self.getTraits())
        print("Ideals: " + self.getIdeals())
        print("Flaws: " + self.getFlaws())
        print("Bonds: " + self.getBonds())
        print("Proficiencies: " + self.getProficiencies())

    def getName(self):
        return self.name
    def getRace(self):
        return self.race
    def getCharClass(self):
        return self.charClass
    def getAlignment(self):
        return self.alignment

    def getAge(self):
        return self.age
    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight

    def getHairColor(self):
        return self.hairColor
    def getEyeColor(self):
        return self.eyeColor
    def getSkinColor(self):
        return self.skinColor

    def getBackground(self):
        return self.background
    def getTraits(self):
        return self.traits
    def getIdeals(self):
        return self.ideals
    def getFlaws(self):
        return self.flaws
    def getBonds(self):
        return self.bonds
    def getProficiencies(self):
        return self.proficiencies

    def setName(self, inName):
        self.name = inName
    def setRace(self, inRace):
        self.race = inRace
    def setCharClass(self, inCharClass):
        self.charClass = inCharClass
    def setAlignment(self, inAlignment):
        self.alignment = inAlignment

    def setAge(self, inAge):
        self.age = inAge
    def setHeight(self, inHeight):
        self.height = inHeight
    def setWeight(self, inWeight):
        self.weight = inWeight

    def setHairColor(self, inHairColor):
        self.charClass = inHairColor
    def setEyeColor(self, inEyeColor):
        self.eyeColor = inEyeColor
    def setSkinColor(self, inSkinColor):
        self.skinColor = inSkinColor

    def setBackground(self, inBackground):
        self.background = inBackground
    def setTraits(self, inTraits):
        self.traits = inTraits
    def setIdeals(self, inIdeals):
        self.ideals = inIdeals
    def setFlaws(self, inFlaws):
        self.flaws = inFlaws
    def setBonds(self, inBonds):
        self.bonds = inBonds
    def setProficiencies(self, inProficiencies):
        self.proficiencies = inProficiencies

    def toString(self):
        self.getBasicChar()
        self.getNumericalChar()
        self.getColorChar()
        self.getAbstractChar()
