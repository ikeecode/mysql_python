import mysql.connector as mc
from me import me


mydb = mc.connect(
    host = 'localhost'
    ,user = 'kaba'
    ,password = me.me
    # ,database = 'Eleves'
)

if mydb:
    mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
# affiche les differentes bases de donnees
for x in mycursor:
    print(x)

choice = input("Enter database name: ")
command = "USE "+ choice
mycursor.execute(command)

mycursor.execute("SHOW TABLES")
# affiches les differentes tables
for x in mycursor:
    print(x)

choice = input("enter table name: ")
mycursor.execute("SELECT * FROM " + choice)
# if mydb:
#     print('ok')
# mycursor = mydb.cursor()
# mycursor.execute("USE Eleves")
# mycursor.execute("SELECT * FROM Eleves")
myresult = mycursor.fetchall()

if myresult:
    for x in myresult:
        print(x)
