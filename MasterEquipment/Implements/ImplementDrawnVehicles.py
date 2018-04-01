from MasterEquipment import DrawnVehicles

drawnVehiclesList = []

#__init__(self, inCategory, inName, inCost, inWeight)
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Barding", "x4", "x2"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Bit and Bridle", "2 gp", "1 lb"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Carriage", "100 gp", "600 lbs"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Cart", "15 gp", "200 lbs"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Chariot", "250 gp", "100 lbs"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Feed (Per Day)", "5 cp", "10 lbs"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Griffon Feed (Per Day)", "20 cp", "10 lbs"))

#Saddles
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("Saddle", "Exotic", "60 gp", "40 lbs"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("Saddle", "Military", "20 gp", "30 lbs"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("Saddle", "Pack", "5 gp", "15 lbs"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("Saddle", "Riding", "10 gp", "25 lbs"))


drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Saddlebags", "4 gp", "8 lbs"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Sled", "20 gp", "300 lbs"))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Stabling (Per Day)", "5 sp", ""))
drawnVehiclesList.append(DrawnVehicles.DrawnVehicles("", "Wagons", "35 gp", "400lbs"))


#for x in drawnVehiclesList:
 #   print (x.toString())