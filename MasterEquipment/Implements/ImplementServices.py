from MasterEquipment import Services

servicesList = []

# __init__(self, inCategory, inName, inCost, inWeight, inPay)

#Coach Cab
servicesList.append(Services.Services("Coach Cab", "Between Towns", "3 cp per Mile", "", ""))
servicesList.append(Services.Services("Coach Cab", "Within a City", "1 cp", "", ""))

#Hireling
servicesList.append(Services.Services("Hireling", "Skilled", "2 gp per Day", "", ""))
servicesList.append(Services.Services("Hireling", "Untrained", "2 sp per Day", "", ""))

servicesList.append(Services.Services("", "Messenger", "2 cp per Mile", "", ""))
servicesList.append(Services.Services("", "Road Toll", "1 cp", "", ""))
servicesList.append(Services.Services("", "Gate Toll", "1 cp", "", ""))
servicesList.append(Services.Services("", "Ship's Passage", "1 sp per Mile", "", ""))

for x in servicesList:
    print(x.toString())