from MasterEquipment import Waterborne

waterborneList = []

#_init_Waterborne(self, inCategory, inCost, inWeight, inSpeed)
waterborneList.append(Waterborne.Waterborne("Galley","30,000 gp","","4 mph"))
waterborneList.append(Waterborne.Waterborne("Keelboat","3,000 gp","","1 mph"))
waterborneList.append(Waterborne.Waterborne("Longship","10,000 gp","","3 mph"))
waterborneList.append(Waterborne.Waterborne("Rowboat","50 gp","","1.5 mph"))
waterborneList.append(Waterborne.Waterborne("Sailing Ship","10,000 gp","","2 mph"))
waterborneList.append(Waterborne.Waterborne("Warship","25,000 gp","","2.5 mph"))

for x in waterborneList:
    print(x.toString())