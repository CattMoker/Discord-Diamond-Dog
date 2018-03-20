class Equipment:
    #basic characteristics
    name = None
    subName = None
    
    #numerical characteristics
    cost = None
    weight = None
    
        def Equipment(self):
            #basic characteristics
            name = ""
            subName = ""

            #numerical characteristics 
            cost = ""
            weight = ""
        
        def Equipment(self, inName, inSubName, inCost, inWeight)
            #basic characteristics
            self.name = inName
            self.subName = inSubName

            #numerical characteristics
            self.cost = inCost
            self.weight = inWeight

        #Chunked Setters
        def SetBaseChar(self, inName, inSubName)
            self.setName(inName)
            self.setSubName(inSubName)

        def SetNumerChar(self, inCost, inWeight)
            self.setCost(inCost)
            self.setWeight(inWeight)

        #Chunked Getters
        def GetBaseChar(self)
            print ("Name: " + self.getName())
            print ("Sub-Name: " + self.getSubName())
        
        def GetNumChar(self)
            print ("Cost: " + self.getCost())
            print ("Weight: " + self.getWeight())
        

        #basic
        def getName(self):
            return self.name
        def getSubName(self):
            return self.subName
        
        #num
        def getCost(self):
            return self.subName
        def getWeight(self):
            return self.weight



        #basic
        def setName(self, inName):
            self.name = inName
        def setSubName(self, inSubName):
           self.subName = inSubName

        #num
        def setCost(self, inCost)
            self.cost = inCost
        def setWeight(self, inWeight)
            self.weight = inWeight


        def toString(self):
            self.GetBaseChar()
            self.GetNumChar()


        


        







