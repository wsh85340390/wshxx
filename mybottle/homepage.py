from bottle import route,run,request
import sqlite3
import sub
@route('/')
def index():
    homepage="""
<html>
<head>
</head>
<body>
<form action="/sub" method="GET">
请填写你的序号：<input type="text" size="20" maxlength="100" name="id"><br>
请填写你的成绩：<input type="text" size="20" maxlength="100" name="grade"><br>
<input type="submit" name="save" value="save">
</form>
</body>
</html>
"""
    return homepage






run(host='localhost', port=8080)
