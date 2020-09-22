
import sqlite3

con = sqlite3.connect("Data.db")

cur = con.cursor()

table = cur.execute("""
CREATE TABLE Details (
   Employee ID  INTEGER,
   First Name TEXT,
   Last Name TEXT,
   Age INTEGER,
   Salary INTEGER
);
""")
con.commit()
con.close()
