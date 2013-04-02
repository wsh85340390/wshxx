from bottle import route, run
import sqlite3
def showstr():  
    db=sqlite3.connect('sy.db')
    cs=db.cursor()
    sqlstr="select  * from sy"
    cs.execute(sqlstr)
    ls=cs.fetchall()
    return ls[:]

head_text="""
<html>
<head>
<title>数据库</title>
</head>
<body>
<table border='1'>"""

foot_text="""
</table></body></html>
"""

def show():
    global head_text
    global foot_text
    strshow=showstr()
    show=""
    show=show+head_text+"<tr>"
    for i in strshow:
        show=show+"<td>"+str(i[0])+":"+str(i[1])+"</td>"
    show=show+"</tr>"+foot_text
    return show

@route('/show')
def index():
    ssh=show()
    return ssh






