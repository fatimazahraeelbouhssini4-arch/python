# ============ CLASSES MÈRES ============

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Age: {self.age}")


class Salarie(Personne):
    def __init__(self, nom, age, numero_somme, salaire):
        super().__init__(nom, age)
        self.numero_somme = numero_somme
        self.salaire = salaire

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Numéro: {self.numero_somme}, Salaire: {self.salaire}")

    def calculer_salaire(self):
        print(f"Salaire calculé: {self.salaire} DH")


class Etudiant(Personne):
    def __init__(self, nom, age, cne, notes):
        super().__init__(nom, age)
        self.cne = cne
        self.notes = notes

    def afficher_infos(self):
        super().afficher_infos()
        print(f"CNE: {self.cne}, Notes: {self.notes}")

    def calculer_moyenne(self):
        print(f"Moyenne: {sum(self.notes) / len(self.notes)}")


# ============ HÉRITAGE MULTIPLE ============

class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, age, numero_somme, salaire, cne, notes, departement, annee_inscription):
        # Initialisation des classes parents
        super().__init__(nom, age, numero_somme, salaire)
        self.cne = cne
        self.notes = notes
        self.departement = departement
        self.annee_inscription = annee_inscription

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Département: {self.departement}, Année: {self.annee_inscription}")


# ============ UTILISATION ============

print("===== Salarie =====")
s = Salarie("Ahmed", 35, "S001", 8000)
s.afficher_infos()
s.calculer_salaire()

print("\n===== Etudiant =====")
e = Etudiant("Sara", 22, "CNE123", [15, 17, 14])
e.afficher_infos()
e.calculer_moyenne()

print("\n===== Doctorant =====")
d = Doctorant("Med", 28, "D001", 5000, "CNE999", [18, 16, 19], "Informatique", 2023)
d.afficher_infos()
s.calculer_salaire()