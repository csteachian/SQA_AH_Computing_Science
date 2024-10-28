# Test the SQL connector package

import mysql.connector

con = mysql.connector.connect(user='root', password='toor', host='127.0.0.1', database='sloco')
c = con.cursor()

c.execute("""SELECT * FROM client""")

for row in c:
  print('Client ID', row[0])
  print('Name', row[1])
  print('Address', row[2])
  print('PhoneNo', row[3])
  print('FaxNo', row[4])
c.close()