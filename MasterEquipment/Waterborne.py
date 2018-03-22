from MasterEquipment.Equipment import Equipment as Equipment

class Waterborne(Equipment):
    speed = None

    def _init_Waterborne(self):
        speed = ""
   
    def _init_Waterborne(self, inCategory, inCost, inWeight, inSpeed):
        super().__init__(inCategory, inCost, inWeight)

        self.speed = inSpeed
    
    def getSpeed(self):
        return self.speed
  
    def setSpeed(self, inSpeed):
        self.speed = inSpeed







    

