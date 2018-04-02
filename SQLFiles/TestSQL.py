import sqlite3
import itertools

# Create a database in RAM
conn = sqlite3.connect('../Equipment.db')
cur = conn.cursor()

potato = []

for row in cur.execute('SELECT * FROM Armor'):
    print(str(row))
