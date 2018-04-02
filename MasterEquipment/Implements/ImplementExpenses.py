from MasterEquipment import LifeExpenses

expenseList = []

#__init__(self, inCategory, inCost, inWeight, inPrice)
expenseList.append(LifeExpenses.LifeExpenses("Wretched", "", "", "-"))
expenseList.append(LifeExpenses.LifeExpenses("Squalid", "", "", "1 sp per day"))
expenseList.append(LifeExpenses.LifeExpenses("Poor", "", "", "2 sp per day"))
expenseList.append(LifeExpenses.LifeExpenses("Modest", "", "", "1 gp per day"))
expenseList.append(LifeExpenses.LifeExpenses("Comfortable", "", "", "2 gp per day"))
expenseList.append(LifeExpenses.LifeExpenses("Wealthy", "", "", "4 gp per day"))
expenseList.append(LifeExpenses.LifeExpenses("Aristocratic", "", "", "10 gp per day minimum"))
