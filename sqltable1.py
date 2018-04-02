import sqlite3
# Create a database in RAM
db = sqlite3.connect('armor.db')
# Creates or opens a file called mydb with a SQLite3 DB

# Get a cursor object
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE Armor(
id INT(9) PRIMARY KEY AUTOINCREMENT ,
category VARCHAR(30),
name VARCHAR(30),
cost VARCHAR(30),
armorclass VARCHAR(30),
strength VARCHAR(30),
stealth VARCHAR(30),
weight VARCHAR(30)
)
''')
cursor.execute('''
CREATE TABLE AdventuringGear(
id INT(9) PRIMARY KEY AUTOINCREMENT ,
category VARCHAR(30),
name VARCHAR(30),
cost VARCHAR(30),
weight VARCHAR(30)
)
''')

cursor.execute('''
CREATE TABLE ContainerCapacity(
id INT(9) PRIMARY KEY AUTOINCREMENT ,
category VARCHAR(30),
capacity VARCHAR(30)
)
''')

cursor.execute('''
CREATE TABLE DrawnVehicles(
id INT(9)PRIMARY KEY AUTOINCREMENT ,
category VARCHAR(30),
name VARCHAR(30),
cost VARCHAR(30),
weight VARCHAR(30)
)
''')
db.commit()
db.close()


