# Définition de la classe (OBLIGATOIRE EN PREMIER)
class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    def presentation(self):
        return f"Je suis {self.nom}, {self.age} ans"

# Création d'une instance
personne1 = Personne('Alice', 28, 'alice@email.com')

# LECTURE des attributs (notation pointée)
print(f"Nom: {personne1.nom}")          # Affiche: Alice
print(f"Âge: {personne1.age}")          # Affiche: 28
print(f"Email: {personne1.email}")      # Affiche: alice@email.com

# MODIFICATION des attributs
personne1.nom = 'Alice Dubois'      # Changement du nom
personne1.age += 1                    # Incrémentation de l'âge
personne1.email = 'alice.dubois@email.com'  # Nouvel email

# Vérification des changements
print(f"Nouveau nom: {personne1.nom}")  # Alice Dubois
print(f"Nouvel âge: {personne1.age}")   # 29