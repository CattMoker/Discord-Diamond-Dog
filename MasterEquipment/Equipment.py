class Equipment:
    #basic characteristics
    name = ""

    #numerical characteristics
    cost = ""
    weight = ""

    def __init__(self, inName, inCost, inWeight):
        #basic characteristics
        self.name = inName

        #numerical characteristics
        self.cost = inCost
        self.weight = inWeight

    #basic
    def getName(self):
        return self.name

    #num
    def getCost(self):
        return self.cost
    def getWeight(self):
        return self.weight



    #basic
    def setName(self, inName):
        self.name = inName

    #num
    def setCost(self, inCost):
        self.cost = inCost
    def setWeight(self, inWeight):
        self.weight = inWeight


    def toString(self):
        self.GetBaseChar()
        self.GetNumChar()


        


        







