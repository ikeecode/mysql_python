class Animal:
    name = "Maobé"
    def __init__(self, nom, espece, habitat, ordre):
        self.nom = nom
        self.espece = espece
        self.habitat = habitat
        self.ordre = ordre


    def animal_sound(self):
        print(f"{self.nom} bayil mbeuleee")

    def yayekane(cls):
        print("Je suis une classe Animal !!!!")
        print(Animal.name)

    # yayekane = classmethod(yayekane)

    def present():
        print("""
            Ceci est une classe qui decrit des Animaux vivant au SENEGAL,
            Par la suite on pourra décider de l'élargir vers les autres pays de l'afrique
        """)

    present = staticmethod(present)


class Humain(Animal): #classe fille herite de la classe Animal
    def __init__(self, nom, espece, habitat, ordre, salaire, sexe):
        # Animal.__init__(self, nom, espece, habitat, ordre)
        super().__init__(nom, espece, habitat, ordre)
        self.salaire = salaire
        self.sexe = sexe

    def animal_sound(self):
        print(f"{self.nom} je suis un humain et je kebetu")



class Mouton(Animal):
    def __init__(self, nom, espece, habitat, ordre, pattes):
        super().__init__(nom, espece, habitat, ordre)
        self.pattes = pattes

    def animal_sound(self):
        print(f"Je suis un mouton et je bele")
