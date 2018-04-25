import sqlite3

# Create a database in RAM
db = sqlite3.connect('../Databases/Garden.db')
# Creates or opens a file called mydb with a SQLite3 DB

# Get a cursor object
cursor = db.cursor()

#######################IMPORTANT####################
cursor.execute('''
CREATE TABLE Coffee_Grounds(
id INTEGER PRIMARY KEY AUTOINCREMENT ,
vendor VARCHAR(30), 
weight DOUBLE,
drop_time VARCHAR(30),
name VARCHAR(30),
discord_id VARCHAR(30)
)
''')


db.commit()
db.close()
