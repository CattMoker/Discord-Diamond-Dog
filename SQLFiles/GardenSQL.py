import sqlite3

# class: GardenSQL.py
# purpose: This is the file that makes the garden tables for Garden.py
# note: this file needs to be run once
db = sqlite3.connect('../Databases/Garden.db')


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
