"""
    data insertion
    single record :     cursor.execute("query")
    multiple record:    cursor.executemany(query,values)
                    where,
                            query = "insert table_name into values(%s,%s,...)"
                            values = [(v1.1,v1.2,...),
                                       (v2.1,v2.2,..),
                                       .....
                                       ]

        Note:
                at last "comit()" the database connector to change
                will happen to database.
"""
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythondb"
)

cursor = database.cursor()
try:
    # cursor.execute("create table customer(ID int primary key,Name varchar(30) not null,Address varchar(30) not null)")
    query = "insert into customer values(%s,%s,%s)"
    values = [(101, 'Rhutik','Pimpri'),
              (102, 'Vijay','Chinchwad'),
              (103, 'Vikrant','Dehuroad'),
              (104, 'Anup', 'Akurdi')
              ]
    cursor.executemany(query,values)
    database.commit()
    print("insertion operation succesfully...")
    print(cursor.rowcount,'was inserted')
except:
    # print("Table creation failed.")
    # print("table may be already present in database")
    print("insertion failed...")
