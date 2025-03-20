import sqlite3

conn = sqlite3.connect('1-sqlite3')
c = conn.cursor()
cursor = c.execute("SELECT id, name, salary  FROM Users")
for row in cursor:
    print(row)
conn.close()