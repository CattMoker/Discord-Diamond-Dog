from MasterEquipment import Mounts

mountsList = []

#__init__(self, inCategory, inCost, inWeight, inSpeed, inCarryingCapacity):
mountsList.append(Mounts.Mounts("Camel", "50 gp", "", "50 ft", ""))
mountsList.append(Mounts.Mounts("Donkey", "8 gp", "", "40 ft", ""))
mountsList.append(Mounts.Mounts("Mule", "8 gp", "", "40 ft", ""))
mountsList.append(Mounts.Mounts("Elephant", "200 gp", "", "40 ft", ""))

#Horses
mountsList.append(Mounts.Mounts("Drafting Horse", "50 gp", "", "40 ft", ""))
mountsList.append(Mounts.Mounts("HRiding Horse", "75 gp", "", "60 ft", ""))


mountsList.append(Mounts.Mounts("Mastiff", "25 gp", "", "40 ft", ""))
mountsList.append(Mounts.Mounts("Pony", "30 gp", "", "40 ft", ""))
mountsList.append(Mounts.Mounts("Warhorse", "400 gp", "", "60 ft", ""))


#for x in mountsList:
   # print(x.toString())
