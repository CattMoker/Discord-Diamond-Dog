from MasterEquipment.Equipment import Equipment as Equipment

class Trinkets(Equipment):
    trinkNum = None
    trinkDesc = None

    def _init_Trinkets(self):
        trinkNum = ""
        trinkDesc = ""
   
    def _init_Trinkets(self, inName, inCost, inWeight, inTrinkNum, inTrinkDesc):
        super().__init__(inName, inCost, inWeight)
		
        self.trinkNum = inTrinkNum
        self.trinkDesc = inTrinkDesc
    
    def getTrinkNum(self):
        return self.trinkNum
    def getTrinkDesc(self):
        return self.trinkDesc

    def setTrinkNum(self, inTrinkNum):
        self.trinkNum = inTrinkNum
    def setTrinkDesc (self, inTrinkDesc):
        self.trinkDesc = inTrinkDesc







    

