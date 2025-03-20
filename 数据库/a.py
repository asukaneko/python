import sqlite3

conn = sqlite3.connect('1-sqlite3')
print('Successpully open database')
cur = conn.cursor()
"""cur.execute(
'''CREATE TABLE Users
   (ID   INT   PRIMARY   KEY     NOT NULL,
    NAME                 TEXT    NOT NULL,
    AGE                  INT     NOT NULL,
    GENDER               TEXT,   
    SALARY               REAL);'''
)
"""
print('Successfully create Table')

cur.execute(
'''INSERT INTO Users (ID,NAME,AGE,GENDER,SALARY)
   VALUES (2, 'dlke',132,'Male',21000);''')
cur.execute(
'''INSERT INTO Users (ID,NAME,AGE,GENDER,SALARY)
   VALUES (3, 'DD',123,'S',20101);''')
cur.execute(
'''INSERT INTO Users (ID,NAME,AGE,GENDER,SALARY)
   VALUES (4, 'SD',231,'SD',10982);''')

cursor = cur.execute("SELECT id, name, salary  FROM Users")
for row in cursor:
    print(row)

conn.commit()
conn.close()