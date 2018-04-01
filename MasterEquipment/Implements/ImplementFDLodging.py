from MasterEquipment import FDLodging

lodgingList = []

# __init__(self, inCategory, inName, inCost, inWeight)

#Ale
lodgingList.append(FDLodging.FDLodging("Ale", "Gallon", "2 sp", ""))
lodgingList.append(FDLodging.FDLodging("Ale", "Mug", "4 cp", ""))

lodgingList.append(FDLodging.FDLodging("", "Banquet (Per Person)", "10 gp", ""))
lodgingList.append(FDLodging.FDLodging("", "Loaf of Bread", "2 cp", ""))
lodgingList.append(FDLodging.FDLodging("", "Hunk of Cheese", "1 sp", ""))

#Inn Stay (Per Day)
lodgingList.append(FDLodging.FDLodging("Inn Stay (Per Day)", "Squalid", "7 cp", ""))
lodgingList.append(FDLodging.FDLodging("Inn Stay (Per Day)", "Poor", "1 sp", ""))
lodgingList.append(FDLodging.FDLodging("Inn Stay (Per Day)", "Modest", "5 sp", ""))
lodgingList.append(FDLodging.FDLodging("Inn Stay (Per Day)", "Comfortable", "8 sp", ""))
lodgingList.append(FDLodging.FDLodging("Inn Stay (Per Day)", "Wealthy", "2 gp", ""))
lodgingList.append(FDLodging.FDLodging("Inn Stay (Per Day)", "Aristocratic", "4 gp", ""))

#Meals(Per Day)
lodgingList.append(FDLodging.FDLodging("Meals (Per Day)", "Squalid", "3 cp", ""))
lodgingList.append(FDLodging.FDLodging("Meals (Per Day)", "Poor", "6 cp", ""))
lodgingList.append(FDLodging.FDLodging("Meals (Per Day)", "Modest", "3 sp", ""))
lodgingList.append(FDLodging.FDLodging("Meals (Per Day)", "Comfortable", "5 sp", ""))
lodgingList.append(FDLodging.FDLodging("Meals (Per Day)", "Wealthy", "8 sp", ""))
lodgingList.append(FDLodging.FDLodging("Meals (Per Day)", "Aristocratic", "2 gp", ""))

lodgingList.append(FDLodging.FDLodging("", "Chunk of Meat", "3 sp", ""))

#Wine
lodgingList.append(FDLodging.FDLodging("Wine", "Common (Pitcher)", "2 sp", ""))
lodgingList.append(FDLodging.FDLodging("Wine", "Fine (Bottle)", "10 gp", ""))


#for x in lodgingList:
   # print(x.toString())