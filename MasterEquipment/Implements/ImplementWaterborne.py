from MasterEquipment import Waterborne


class ImplementWaterborne:
    waterborneList = []

    def __init__(self):
        self.waterborneList = []
        self.waterborneList.append(Waterborne.Waterborne("Galley", "30,000 gp", "", "4 mph"))
        self.waterborneList.append(Waterborne.Waterborne("Keelboat", "3,000 gp", "", "1 mph"))
        self.waterborneList.append(Waterborne.Waterborne("Longship", "10,000 gp", "", "3 mph"))
        self.waterborneList.append(Waterborne.Waterborne("Rowboat", "50 gp", "", "1.5 mph"))
        self.waterborneList.append(Waterborne.Waterborne("Sailing Ship", "10,000 gp", "", "2 mph"))
        self.waterborneList.append(Waterborne.Waterborne("Warship", "25,000 gp", "", "2.5 mph"))

    def getList(self):
        return self.waterborneList

    def runList(self, copiedList):
        # _init_Waterborne(self, inCategory, inCost, inWeight, inSpeed)
        for x in self.waterborneList:
            copiedList.append(x)

    def readList(self):
        for x in self.waterborneList:
            print(x.toString())
