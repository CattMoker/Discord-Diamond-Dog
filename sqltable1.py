import sqlite3
# Create a database in RAM
db = sqlite3.connect('Equipment.db')
# Creates or opens a file called mydb with a SQLite3 DB

# Get a cursor object
cursor = db.cursor()

cursor.execute('''
CREATE TABLE Armor(
id INTEGER PRIMARY KEY,
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
id INTEGER PRIMARY KEY,
category VARCHAR(30),
name VARCHAR(30),
cost VARCHAR(30),
weight VARCHAR(30)
)
''')

cursor.execute('''
CREATE TABLE ContainerCapacity(
id INTEGER PRIMARY KEY,
category VARCHAR(30),
capacity VARCHAR(30)
)
''')

cursor.execute('''
CREATE TABLE DrawnVehicles(
id INTEGER PRIMARY KEY,
category VARCHAR(30),
name VARCHAR(30),
cost VARCHAR(30),
weight VARCHAR(30)
)
''')

#########################################################################FDLodging, Mounts, Services and Tools###############################################################
cursor.execute('''
CREATE TABLE FDLodging(
id INTEGER PRIMARY KEY,
category VARCHAR(30),
name VARCHAR(30),
cost VARCHAR(30)
)
''')


cursor.execute('''
CREATE TABLE Mounts(
id INTEGER PRIMARY KEY,
category VARCHAR(30),
cost VARCHAR(30),
speed VARCHAR(30),
carryingcapacity VARCHAR(30)
)
''')

cursor.execute('''
CREATE TABLE Services(
id INTEGER PRIMARY KEY,
category VARCHAR(30),
name VARCHAR(30),
pay VARCHAR(30)
)
''')

cursor.execute('''
CREATE TABLE Tools(
id INTEGER PRIMARY KEY,
category VARCHAR(30),
name VARCHAR(30),
cost VARCHAR(30),
weight VARCHAR(30)
)
''')



db.commit()
db.close()


