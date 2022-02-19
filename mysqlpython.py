import mysql.connector

mydb = mysql.connect(
    host="localhost",
    username="root",
    password=""
)

print(mydb)