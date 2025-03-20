import sqlite3

conn = sqlite3.connect('1-sqlite3')
c = conn.cursor()

c.execute(
'''INSERT INTO Users (ID,NAME,AGE,GENDER,SALARY)
   VALUES (1, 'Mlke',32,'Male',20000);'''
)
conn.commit()
print('Ok')
conn.close()