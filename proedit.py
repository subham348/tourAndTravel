#!C:\Users\USER\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
d=cgi.FieldStorage()
id=int(d.getvalue('id'))
cur.execute("select * from info where id=%d"%(id))
x=cur.fetchone()
print("""
<html>
<body>
<form action="proedit_code.py">
<input type="text" name="a1" value="%s">
<input type="hidden" name="a2" value="%d">
<input type="submit" value="Submit">
</form>
</body>
</html>
"""%(x[1],x[0]))
