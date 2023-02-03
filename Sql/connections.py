import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythondb"
)
print(database)

cursor = database.cursor()
x = input("Enter table name:")
try:
    cursor.execute(f"create table {x}(ID int(10) primary key,Name varchar(30) not null)")
    print("Table created succesfully...")
except:
    print("Table creation failed.")
    print("table may be already present in database")
