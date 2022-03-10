import mysql.connector as mc
from me import me

# connection a la base de donnee
mydb = mc.connect(
    host = 'localhost',
    user = 'kaba',
    password = me.me,
    # database = 'Eleves'
)

# print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("""CREATE TABLE marks(
#     devoir int not null,
#     exam int not null
# )""")
# mycursor.execute("ALTER TABLE marks ADD COLUMN id int auto_increment primary key")
# for x in mycursor:
#     print(x)

sql = "INSERT INTO marks (devoir, exam, matiere) VALUES (%s, %s, %s)"
# val = [
#     (10, 11, "HG"),
#     (11, 13, "Philo"),
#     (12, 12, "ESP"),
#     (13, 17, "ART"),
#     (14, 16, "ESP"),
#     (15, 15, "SVT"),
#     (16, 13, "PORTUGUES"),
#     (17, 13, "PYTHON"),
#     (18, 16, "JAVA"),
#     (19, 13, "JAVASCRIPT"),
#     (20, 19, "ML"),
#     (11, 15, "AI"),
#     (12, 18, "DL"),
#     (13, 18, "NLP"),
#     (14, 20, "SQL"),
#     (15, 19, "MYSQL")
# ]
val = (12, 18, "Physique")
# mycursor.executemany(sql, val) #when you insert a lot of values at once

# mycursor.execute(sql, val)


# mydb.commit() # indispensable pour appliquer les changements

# print(mycursor.rowcount, "record inserted:")
# print(mycursor.lastrowid)

mycursor.execute("SELECT devoir, matiere FROM marks LIMIT 5,10")

myresult = mycursor.fetchone()
#
# for res in myresult:
#     print(res)

print(myresult)


auto = "'Fisker' 'Ford' 'Ford' 'Mustang' 'Fuso' 'GAZ' 'Ginetta' 'GMC' 'Grecav' 'Gumpert' 'Hispano' 'Suiza' 'Hommell' 'Honda'"
