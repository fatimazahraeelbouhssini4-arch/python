class Etudiant:
    def __init__(self, nom, filiere):
        self.nom = nom
        self.filiere = filiere

    def se_presenter(self):
        return f"Je suis {self.nom}, je fais mes études en {self.filiere}"

# création d'un objet
etudiant1 = Etudiant("Fatima", "Informatique")

# appel de la méthode
print(etudiant1.se_presenter())