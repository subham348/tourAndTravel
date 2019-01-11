#!C:\Users\USER\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
d=cgi.FieldStorage()
id=int(d.getvalue('id'))
print(id)
cur.execute("delete from info where id=%d"%(id))
db.commit()