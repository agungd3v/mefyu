import mysql.connector
from mysql.connector import errorcode

try:
  database = mysql.connector.connect(
    host = "127.0.0.1",
    port = "3306",
    user = "root",
    passwd = "root",
    # database = "mefyu",
    raise_on_warnings = True
  )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print("Database connection: OK")
