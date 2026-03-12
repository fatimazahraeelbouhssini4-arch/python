from abc import ABC, abstractmethod
from dataclasses import dataclass

# =========================
# 1. Classe abstraite Boisson
# =========================

class Boisson(ABC):

    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass

    # combinaison de boissons
    def __add__(self, other):
        return BoissonCombinee(self, other)


# =========================
# 2. Boissons concrètes
# =========================

class Cafe(Boisson):

    def cout(self):
        return 2.0

    def description(self):
        return "Café simple"


class The(Boisson):

    def cout(self):
        return 1.5

    def description(self):
        return "Thé"


# =========================
# 3. Classe Decorateur
# =========================

class Ingredient(Boisson):

    def __init__(self, boisson):
        self.boisson = boisson


class Lait(Ingredient):

    def cout(self):
        return self.boisson.cout() + 0.5

    def description(self):
        return self.boisson.description() + ", Lait"


class Sucre(Ingredient):

    def cout(self):
        return self.boisson.cout() + 0.2

    def description(self):
        return self.boisson.description() + ", Sucre"


class Caramel(Ingredient):

    def cout(self):
        return self.boisson.cout() + 0.7

    def description(self):
        return self.boisson.description() + ", Caramel"


# =========================
# 4. Combinaison de boissons
# =========================

class BoissonCombinee(Boisson):

    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    def cout(self):
        return self.b1.cout() + self.b2.cout()

    def description(self):
        return self.b1.description() + " + " + self.b2.description()


# =========================
# 5. Data class Client
# =========================

@dataclass
class Client:
    nom: str
    numero: int
    points: int = 0


# =========================
# 6. Classe Commande
# =========================

class Commande:

    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        total = 0
        for b in self.boissons:
            total += b.cout()
        return total

    def afficher_commande(self):
        print("Client :", self.client.nom)
        print("Boissons :")

        for b in self.boissons:
            print("-", b.description())

        print("Prix total :", self.prix_total(), "€")


# =========================
# 7. Commande sur place
# =========================

class CommandeSurPlace(Commande):

    def afficher_commande(self):
        print("Commande sur place")
        super().afficher_commande()


# =========================
# 8. Commande à emporter
# =========================

class CommandeEmporter(Commande):

    def afficher_commande(self):
        print("Commande à emporter")
        super().afficher_commande()


# =========================
# 9. Programme de fidélité
# =========================

class Fidelite:

    def ajouter_points(self, client, montant):
        points = int(montant)
        client.points += points


# =========================
# 10. Commande avec fidélité
# =========================

class CommandeFidele(Commande, Fidelite):

    def valider_commande(self):
        total = self.prix_total()
        self.ajouter_points(self.client, total)


# =========================
# 11. Test du système
# =========================

if __name__ == "__main__":

    # créer client
    client1 = Client("Fatima", 1)

    # créer boissons
    cafe = Cafe()
    cafe_lait = Lait(cafe)
    cafe_lait_sucre = Sucre(cafe_lait)

    the = The()

    # combinaison
    menu = cafe_lait_sucre + the

    # créer commande
    commande = CommandeFidele(client1)

    commande.ajouter_boisson(menu)

    # afficher
    commande.afficher_commande()

    # valider commande
    commande.valider_commande()

    print("Points fidélité du client :", client1.points)