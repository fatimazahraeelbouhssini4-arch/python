class Vehicule:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse

    def accelerer(self):
        print(f"{self.marque} accélère")

    def freiner(self):
        print(f"{self.marque} freine")


class Voiture(Vehicule):
    def __init__(self, marque, vitesse, nb_portes):
        super().__init__(marque, vitesse)  # Hérite de Vehicule
        self.nb_portes = nb_portes

    # Hérite de accelerer()
    # Hérite de freiner()

    def klaxonner(self):
        print(f"{self.marque} klaxonne")


# Utilisation
unevoiture = Voiture("Peugeot", 0, 5)
unevoiture.accelerer()   # Peugeot accélère
unevoiture.freiner()     # Peugeot freine
unevoiture.klaxonner()   # Peugeot klaxonne