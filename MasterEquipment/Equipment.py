class Equipment:
    #basic characteristics
    category = ""

    #numerical characteristics
    cost = ""
    weight = ""

    def __init__(self, inCategory, inCost, inWeight):
        #basic characteristics
        self.category = inCategory

        #numerical characteristics
        self.cost = inCost
        self.weight = inWeight

    #basic
    def getName(self):
        return self.category

    #num
    def getCost(self):
        return self.cost
    def getWeight(self):
        return self.weight



    #basic
    def setName(self, inCategory):
        self.category = inCategory

    #num
    def setCost(self, inCost):
        self.cost = inCost
    def setWeight(self, inWeight):
        self.weight = inWeight


    def toString(self):
        self.GetBaseChar()
        self.GetNumChar()


        


        







