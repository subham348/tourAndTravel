#!C:\Users\USER\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
d=cgi.FieldStorage()
a=int(d.getvalue('a2'))
b=d.getvalue('a1')
cur.execute("update info set name='%s' where id=%d"%(b,a))
db.commit()
