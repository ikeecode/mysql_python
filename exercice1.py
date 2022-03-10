import mysql.connector as mc
from random import randint, choice, shuffle
from datetime import datetime
from sys import exit

mydb = mc.connect(option_files = "my.ini")
mycursor = mydb.cursor()
# mycursor.execute("ALTER TABLE reference AUTO_INCREMENT = 1")
# mycursor.execute("ALTER TABLE pieces AUTO_INCREMENT = 1")
# mycursor.execute("ALTER TABLE vehicules AUTO_INCREMENT = 1")

# recuperation des ids qui sonts dans correspond
mycursor.execute("SELECT * FROM correspond")
idcorrespond = mycursor.fetchall()
# for x in idcorrespond:
#     print(x)

# exit()

insert_reference  = "INSERT INTO reference (prix) VALUES (%s)"
insert_pieces     = "INSERT INTO pieces (categories, dates, id_ref) VALUES (%s, %s, %s)"
insert_vehicules  = "INSERT INTO vehicules (marque, annee, modele) VALUES (%s, %s, %s)"
insert_correspond = "INSERT INTO correspond (id_piece, id_vehicule) VALUES (%s, %s)"


# generateur de reference pour la base de donnee
def data_reference(n:int):
    ref = []
    # n est la taille de la liste de donnee à retourner
    for x in range(n):
        ref.append((randint(0, 200_000),))
    return ref

# generateur de pieces pour la base de donnee
def data_pieces(n:int, idref_range):
    pieces = []
    categories = ['carrosserie', 'garnissage',
                  'vitrage', 'optique',
                  'mécanique', 'electronique',
                  'electrique', 'organes de freinage']
    for x in range(n):
        date  = datetime(randint(1960, 2022), randint(1, 12), randint(1, 28))
        idref = choice(idref_range)
        categorie = choice(categories)
        pieces.append((categorie, date, idref))

    return pieces

# generateur de vehicules pour la base de donnee
def data_vehicule(n:int):
    vehic = []
    modeles = ['coupés', 'berlines', 'hayons', 'type-break',
                'limousines', 'pick-up', 'crossovers',
                'type-SUV', 'fourgonnettes', 'mini-fourgonnettes',
                 'carrosserie', 'liftback', 'cabriolets', 'minibus',
                 'roadsters', 'type-targa']
    auto   = ['Fisker', 'Ford', 'Ford', 'Mustang', 'Fuso',
                'GAZ', 'Ginetta', 'GMC', 'Grecav', 'Gumpert',
                'Hispano', 'Suiza', 'Hommell', 'Honda']
    for x in range(n):
        marque = choice(auto)
        modele = choice(modeles)
        annee  = randint(1960, 2022)
        vehic.append((marque, annee, modele))

    return vehic

# generateur de correspondance pour la base de donnee
def data_correspond(idvehicules, idpieces):
    v = idvehicules.copy()
    p = idpieces.copy()
    n = len(v)
    m = len(p)
    match = []
    for x in range(n*m):
        shuffle(v)
        shuffle(p)
        vehic = choice(v)
        piece = choice(p)
        if (piece, vehic) not in match and (piece, vehic) not in idcorrespond:
            match.append((piece, vehic))

    return match


# insertion des references
reference = data_reference(10)
mycursor.executemany(insert_reference, reference)

# recuperation des ids dans reference
mycursor.execute("SELECT reference.id_ref FROM reference")
idref_range = mycursor.fetchall()
idref_range = [i[0] for i in idref_range]
# print(idref_range)


# insertion des pieces
pieces = data_pieces(10, idref_range)
mycursor.executemany(insert_pieces, pieces)

# insertion des vehicules
vehicules  = data_vehicule(20)
mycursor.executemany(insert_vehicules, vehicules)

# recuperation des ids vehicule et piece
mycursor.execute("SELECT vehicules.id_vehicule FROM vehicules")
idvehicules = mycursor.fetchall()
idvehicules = [i[0] for i in idvehicules]

mycursor.execute("SELECT pieces.id_piece FROM pieces")
idpieces = mycursor.fetchall()
idpieces = [i[0] for i in idpieces]

# # insertion des correspondances
correspond = data_correspond(idvehicules, idpieces)
# print(correspond)
mycursor.executemany(insert_correspond, correspond)

print(mycursor.rowcount, '-lignes insérés...') # le nombre de lignes inserés

# print("Affichage de notre insertion : ")
# mycursor.execute("SELECT * FROM correspond")
# for x in mycursor.fetchall():
#     print(x)
# print(mycursor.fetchall())

mydb.commit() #decommenter pour valider les changements
mydb.close()
print('db closed.')
