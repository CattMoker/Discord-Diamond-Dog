from MasterEquipment.Equipment import Equipment
from MasterEquipment import Weapons

weaponList = []
#(self, inName, inSubName, inCost, inWeight, inDamage, inProperties)
# Simple Melee Weapons
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Club", "1 sp", "2 lb.", "1d4 bludgeoning", "Light"))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Dagger", "2 gp", "1 lb.", "1d4 piercing", "Finesse, light, thrown (range(20/60))"))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Greatclub", "2 sp", "10 lb.", "1d8 bludgeoning", "Two-handed"))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Handaxe", "5 gp", "2 lb.", "1d6 slashing", "Light, thrown (range 20/60)"))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Javelin", "5 sp", "2 lb.", "1d6 piercing", "Thrown (range 30/120)"))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Light hammer", "2 gp", "2 lb.", "1d4 bludgeoning", "Light, thrown (range20/60)"))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Mace", "5 gp", "4 lb.", "1d6 bludgeoning", ""))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Quarterstaff", "2 sp", "4 lb.", "1d6 bludgeoning", "Versatile (1d8)"))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Sickle", "1 gp", "2 lb.", "1d4 slashing", "Light"))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Spear", "1 gp", "3 lb.", "1d6 piercing", "Thrown (range 20/60), versatile (1d8)"))

#Simple Ranged Weapons
weaponList.append(Weapons.Weapons("Simple Ranged Weapons", "Crossbow, light", "25 gp", "5 lb.", "1d8 piercing", "Ammunition (range 80/320), loading, two-handed"))
weaponList.append(Weapons.Weapons("Simple Ranged Weapons", "Dart", "5 cp", "1/4 lb.", "1d4 piercing", "Finesse, thrown (range 20/60)"))
weaponList.append(Weapons.Weapons("Simple Ranged Weapons", "Shortbow", "25 gp", "2 lb.", "1d6 piercing", "Ammunition (range 80/320), two-handed"))
weaponList.append(Weapons.Weapons("Simple Ranged Weapons", "Sling", "1 sp", "", "1d4 bludgeoning", "Ammunition (range 30/120)"))

# Martial Melee Weapons
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Battleaxe", "10 gp", "4 lb.", "1d8 slashing", "Versatile (1d10)"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Flail", "10 gp", "2 lb.", "1d8 bludgeoning", ""))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Glaive", "20 gp", "6 lb.", "1d10 slashing", "Heavy, reach, two-handed"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Greataxe", "30 gp", "7 lb.", "1d12 slashing", "Heavy, two-handed"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Greatsword", "50 gp", "6 lb.", "2d6 slashing", "Heavy, two-handed"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Halberd", "20 gp", "6 lb.", "1d10 slashing", "Heavy, reach, two-handed"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Lance", "10 gp", "6 lb.", "1d12 piercing", "Reach, special"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Longsword", "15 gp", "3 lb.", "1d8 slashing", "Versatile (1d10)"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Maul", "10 gp", "10 lb.", "2d6 bludgeoning", "Heavy, two-handed"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Morningstar", "15 gp", "4 lb.", "1d8 piercing", ""))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Pike", "5 gp", "18 lb.", "1d10 piercing", "Heavy, reach, two-handed"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Rapier", "25 gp", "2 lb.", "1d8 piercing", "Finesse"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Scimitar", "25 gp", "3 lb.", "1d6 slashing", "Finesse, light"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Shortsword", "10 gp", "2 lb.", "1d6 piercing", "Finesse, light"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Trident", "5 gp", "4 lb.", "1d6 piercing", "Thrown (range 20/60), versatile (1d8)"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "War pick", "5 gp", "2 lb.", "1d8 piercing", ""))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Warhammer", "15 gp", "7 lb.", "1d8 bludgeoning", "Versatile (1d10)"))
weaponList.append(Weapons.Weapons("Martial Melee Weapons", "Whip", "2 gp", "3 lb.", "1d4 slashing", "Finesse, reach"))

# Martial Ranged Weapons
weaponList.append(Weapons.Weapons("Martial Ranged Weapons", "Blowgun", "10 gp", "1 lb.", "1 piercing", "Ammunition (range 25/100), loading"))
weaponList.append(Weapons.Weapons("Martial Ranged Weapons", "Crossbow, hand", "75 gp", "3 lb.", "1d6 piercing", "Ammunition (range 30/120), light, loading"))
weaponList.append(Weapons.Weapons("Martial Ranged Weapons", "Crossbow, heavy", "50 gp", "18 lb.", "1d10 piercing", "Ammunition (range 100/400), heavy, loading, two-handed"))
weaponList.append(Weapons.Weapons("Martial Ranged Weapons", "Longbow", "50 gp", "2 lb.", "1d8 piercing", "Ammunition (range 150/600), heavy, two-handed"))
weaponList.append(Weapons.Weapons("Martial Ranged Weapons", "Net", "1 gp", "3 lb.", "", "Special, thrown (range 5/15)"))











