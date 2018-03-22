from MasterEquipment.Equipment import Equipment
from MasterEquipment import Weapons

weaponList = []
#(self, inName, inSubName, inCost, inWeight, inDamage, inProperties)
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Club", "1 gp", "2 lb.", "1d4 bludgeoning", "Light"))
weaponList.append(Weapons.Weapons("Simple Melee Weapons", "Dagger", "2 gp", "1 lb.", "1d4 piercing", "Finesse, light, thrown (range(20/60))"))
weaponList.append(Weapons.Weapons())
