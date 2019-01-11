#!C:\Users\USER\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-type:text/html\r\n\r\n")
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
cur.execute("select * from info")
x=cur.fetchall()
print("""
<html>
<style>
td
{
height:50px;
width:200px;
background-color:yellow;
text-align:center;
}
</style>
<body bgcolor="green" align="center"><br><br><br><br><br>
<table border=5 align="center">
""")
for i in x:
	print("""
	<tr><td><a href="prodescrip.py?id=%d">%s</a></td></tr>
	"""%(i[0],i[1]))
print("""
</table>
</body>
</html>
""")
