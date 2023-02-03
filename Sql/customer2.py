"""
    Data Visualization

        single row:
                        cursor.fetchone()

        all rows:
                        cursor.fetchall() 

"""
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythondb"
)

cursor = database.cursor()

cursor.execute("select * from customer")
result = cursor.fetchall()

for r in result:
    print(r)