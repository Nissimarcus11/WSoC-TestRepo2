import sqlite3

con = sqlite3.connect("Data.db")

cur = con.cursor()
cur.execute(
    "select * from Details"
)
list = cur.fetchall()
for i in list:
    print(i)


con.close()