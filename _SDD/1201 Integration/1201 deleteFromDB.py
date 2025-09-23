# Test the SQL connector package

import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='sloco')
c = con.cursor()

c.execute("""DELETE FROM client WHERE Client_ID = 3""")
con.commit() # note it is connection, not cursor here
c.close()

# Can you add a line to show how many records have been deleted?