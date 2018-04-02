import sqlite3
#from MasterEquipment.Equipment import Equipment
from MasterEquipment import Armor

armorList = []
#(self, inName, inSubName, inCost, inWeight, inArmorClass, inStrength, inStealth)
#Light Armors
armorList.append(Armor.Armor("Light Armor", "Padded", "5 gp", "8 lb", "11 + Dex modifier", "", "Disadvantage"))
armorList.append(Armor.Armor("Light Armor", "Leather", "10 gp", "10 lb", "11 + Dex modifier", "", ""))
armorList.append(Armor.Armor("Light Armor", "Studded Leather", "45 gp", "13 lb", "12 + Dex modifier", "", ""))
#Medium Armors
armorList.append(Armor.Armor("Medium Armor", "Hide", "10 gp", "12 lb", "12 + Dex modifier (max 2)", "", ""))
armorList.append(Armor.Armor("Medium Armor", "Chain shirt", "50 gp", "20 lb", "13 + Dex modifier (max 2)", "", ""))
armorList.append(Armor.Armor("Medium Armor", "Scale mail", "50 gp", "45 lb", "14 + Dex modifier (max 2)", "", "Disadvantage"))
armorList.append(Armor.Armor("Medium Armor", "Breastplate", "400 gp", "20 lb", "14 + Dex modifier (max 2)", "", ""))
armorList.append(Armor.Armor("Medium Armor", "Half plate", "750 gp", "40 lb", "15 + Dex modifier (max 2)", "", "Disadvantage"))
#Heavy Armors
armorList.append(Armor.Armor("Heavy Armor", "Ring mail", "30 gp", "40 lb", "14", "", "Disadvantage"))
armorList.append(Armor.Armor("Heavy Armor", "Chain mail", "75 gp", "55 lb", "16", "Str 13", "Disadvantage"))
armorList.append(Armor.Armor("Heavy Armor", "Splint", "200 gp", "60 lb", "17", "Str 15", "Disadvantage"))
armorList.append(Armor.Armor("Heavy Armor", "Plate", "1500 gp", "65 lb", "18", "Str 15", "Disadvantage"))
#Shield
armorList.append(Armor.Armor("Shield", "Shield", "10 gp", "6 lb", "+2", "", ""))

# Create a database in RAM
db = sqlite3.connect('../../Equipment.db')
# Creates or opens a file called mydb with a SQLite3 DB

# Get a cursor object
cursor = db.cursor()
#for x in armorList:
#    cursor.execute("INSERT INTO Armor (category, name, cost, armorclass, strength, stealth, weight) VALUES (?,?,?,?,?,?,?)",
#                   (x.getCategory(), x.getName(), x.getCost(), x.getArmorClass(), x.getStrength(), x.getStealth(), x.getWeight()))
#cursor.execute("DELETE FROM Armor")
cursor.execute("SELECT * FROM Armor")
print(cursor.fetchall())
db.commit()
db.close()
#for x in armorList:
 #   print(x.toString())

