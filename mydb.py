# Install Mysql On Your Computer
# http://dev.mysql.com/download/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE musker")

print("ALL DONE!")
