import show
from bottle import route,run,request
import sqlite3

@route('/sub',method='GET')
def submitit():
    if request.GET.get('save','').strip():
        newid = request.GET.get('id', '').strip()
        newgrade=request.GET.get('grade','').strip()
        print(newid)
        db=sqlite3.connect('sy.db')
        c = db.cursor()
        sqlstr="""insert into sy (id, name) values("""+newid+""",'"""+newgrade+"""')"""
        print(sqlstr)
        c.execute(sqlstr)
        db.commit()
        c.close()
        return """
<html>
<head>
</head>
<body>
"""+'成绩%s已经添加！' % newid+"""
<a href="show">show</a>
</body>

"""
    else:
        return '成绩添加失败！'
