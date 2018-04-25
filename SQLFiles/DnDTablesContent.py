import sqlite3

# Create a database in RAM
db = sqlite3.connect('../Databases/Equipment.db')
# Creates or opens a file called mydb with a SQLite3 DB

from MasterEquipment.Implements import ImplementExpenses, ImplementDrawnVehicles, ImplementArmor, ImplementFDLodging, ImplementMounts, ImplementsAdventuringGear, ImplementServices, ImplementTools, ImplementTradeGoods, ImplementTrinkets, ImplementWaterborne, ImplementWeapons

#done
cursor = db.cursor()
for x in ImplementArmor.armorList:
   cursor.execute("INSERT INTO Armor (category, name, cost, armorclass, strength, stealth, weight) VALUES (?,?,?,?,?,?,?)",
                  (x.getCategory(), x.getName(), x.getCost(), x.getArmorClass(), x.getStrength(), x.getStealth(), x.getWeight()))
# cursor.execute("DELETE FROM Armor")
cursor.execute("SELECT * FROM Armor")
print("Armor: ")
print(cursor.fetchall())
db.commit()
db.close()


#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementDrawnVehicles.drawnVehiclesList:
   cursor.execute("INSERT INTO DrawnVehicles (category, name, cost, weight) VALUES (?,?,?,?)",
                  (x.getCategory(), x.getName(), x.getCost(), x.getWeight()))
# cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM DrawnVehicles")
print("Drawn Vehicles: ")
print(cursor.fetchall())
db.commit()
db.close()


#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementExpenses.expenseList:
    cursor.execute("INSERT INTO Expenses (category, price) VALUES (?,?)",
                   (x.getCategory(), x.getPrice()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM Expenses")
print("Expenses: ")
print(cursor.fetchall())
db.commit()
db.close()


#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementFDLodging.lodgingList:
    cursor.execute("INSERT INTO FDLodging (category, name, cost) VALUES (?,?,?)",
                   (x.getCategory(), x.getName(), x.getCost()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM FDLodging")
print("FDLodging: ")
print(cursor.fetchall())
db.commit()
db.close()

#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementMounts.mountsList:
    cursor.execute("INSERT INTO Mounts (category, cost, speed, carryingcapacity) VALUES (?,?,?,?)",
                   (x.getCategory(), x.getCost(), x.getSpeed(), x.getCarryingCapacity()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM Mounts")
print("Mounts: ")
print(cursor.fetchall())
db.commit()
db.close()


#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementsAdventuringGear.adventuringGear:
    cursor.execute("INSERT INTO AdventuringGear (category, name, cost, weight) VALUES (?,?,?,?)",
                   (x.getCategory(), x.getName(), x.getCost(), x.getWeight()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM AdventuringGear")
print("Adventuring Gear: ")
print(cursor.fetchall())
db.commit()
db.close()

#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementServices.servicesList:
    cursor.execute("INSERT INTO Services (category, name, pay) VALUES (?,?,?)",
                   (x.getCategory(), x.getName(), x.getPay()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM Services")
print("Services: ")
print(cursor.fetchall())
db.commit()
db.close()

#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementTools.toolsList:
    cursor.execute("INSERT INTO Tools (category, name, cost, weight) VALUES (?,?,?,?)",
                   (x.getCategory(), x.getName(), x.getCost(), x.getWeight()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM Tools")
print("Tools: ")
print(cursor.fetchall())
db.commit()
db.close()

#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementTradeGoods.tradeGoodList:
    cursor.execute("INSERT INTO TradeGoods (cost, goods) VALUES (?,?)",
                   (x.getCost(), x.getGoods()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM TradeGoods")
print("Trade Goods: ")
print(cursor.fetchall())
db.commit()
db.close()

#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementTrinkets.trinketsList:
    cursor.execute("INSERT INTO Trinkets (trinkNum, trinkDesc) VALUES (?,?)",
                   (x.getTrinkNum(), x.getTrinkDesc()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM Trinkets")
print("Trinkets: ")
print(cursor.fetchall())
db.commit()
db.close()

#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementWaterborne.waterborneList:
    cursor.execute("INSERT INTO Waterborne (category, cost, speed) VALUES (?,?,?)",
                   (x.getCategory(), x.getCost(), x.getSpeed()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM Waterborne")
print("Waterborne")
print(cursor.fetchall())
db.commit()
db.close()

#done
db = sqlite3.connect('../Databases/Equipment.db')
cursor = db.cursor()
for x in ImplementWeapons.weaponList:
    cursor.execute("INSERT INTO Weapons (category, name, cost, damage, weight, properties) VALUES (?,?,?,?,?,?)",
                   (x.getCategory(), x.getName(), x.getCost(), x.getDamage(), x.getWeight(), x.getProperties()))
    #cursor.execute("DELETE FROM DrawnVehicles")
cursor.execute("SELECT * FROM Weapons")
print("Weapons: ")
print(cursor.fetchall())
db.commit()
db.close()
