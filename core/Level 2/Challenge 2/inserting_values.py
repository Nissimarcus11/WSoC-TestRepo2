import sqlite3

con = sqlite3.connect("Data.db")

cur = con.cursor()

data = [
    ("1","Evelyn","Grace","26","280$"),
    ("2","Olivia","Harper","28","320$"),
    ("3","Robert","Hall","24","310$"),
    ("4","Doug","Judy","32","370$"),
    ("5","Leo","Valdez","22","270$")
] #storing the data in the form of list
for i in data:
    cmd = """ INSERT INTO Details 
    VALUES ("{emp_id}","{fname}","{lname}","{age}","{salary}");
    """ #creating a template for sqlcommand
    sql_cmd = cmd.format(emp_id=i[0],fname=i[1],lname=i[2],age=i[3],salary=i[4]) #updating values
    cur.execute(sql_cmd)  #executing sql commands
    
con.commit()
con.close()

