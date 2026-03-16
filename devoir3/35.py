class Vehicule:
    def demarrer(self):
        print("Vehicule")


class Voiture(Vehicule):
    def demarrer(self):
        print("Voiture")


class Moto(Vehicule):
    def demarrer(self):
        print("Moto")


vehicules = [Voiture(), Moto()]

for v in vehicules:
    v.demarrer()
