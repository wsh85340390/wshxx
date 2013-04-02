import sqlite3
db=sqlite3.connect('sy.db')
cs=db.cursor()
sqlstr="select  * from sy"
cs.execute(sqlstr)
ls=cs.fetchall()
print(ls)
