import sqlite3
import itertools

# class: TestSQL
# purpose: this class was just to test sqlite in python
conn = sqlite3.connect('../Equipment.db')
cur = conn.cursor()

potato = []

for row in cur.execute('SELECT * FROM Armor'):
    print(str(row))
