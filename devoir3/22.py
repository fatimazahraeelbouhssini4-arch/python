class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.pages = 0   # valeur par défaut

# Création d'objet
mon_livre = Livre("Python Facile", "Ali", 2024)