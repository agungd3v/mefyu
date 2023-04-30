from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from config.database import database
from database.schema import users, posts

DB_NAME = "mefyu"

TABLES = {}
TABLES[users] = users
TABLES[posts] = posts

cnx = database
cursor = cnx.cursor()

def create_database(cursor):
  try:
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
  except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
    exit(1)

try:
  cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
  print("Database {} does not exists.".format(DB_NAME))
  if err.errno == errorcode.ER_BAD_DB_ERROR:
    create_database(cursor)
    print("Database {} created successfully.".format(DB_NAME))
    cnx.database = DB_NAME
  else:
    print(err)
    exit(1)

for table_name in TABLES:
  table_description = TABLES[table_name]
  try:
    print("Creating table {}: ".format(table_name), end="")
    cursor.execute(table_description)
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
      print("already exists.")
    else:
      print(err.msg)
  else:
    print("OK")

cursor.close()
cnx.close()
