# mySQL Connector SloCo INSERT Program
# Ian Simpson, October 2019

import mysql.connector
    
con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='sloco')
c = con.cursor()

sqlstatement = "INSERT INTO `client` (`Client_ID`, `Name`, `Address`, `PhoneNo`, `FaxNo`) VALUES ('3', 'Dottore Ettore Ferrari', 'Via San Siro 18', '0223789543', '0278397895');"

c.execute(sqlstatement)

con.commit() # note it is connection, not cursor here

print(c.rowcount,"record inserted")

c.close()