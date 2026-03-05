class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        """Getter pour la longueur"""
        return self._longueur

    @property
    def aire(self):
        """Calcul de l'aire à la volée"""
        return self._longueur * self._largeur

    @property
    def perimetre(self):
        """Calcul du périmètre"""
        return 2 * (self._longueur + self._largeur)

# Utilisation naturelle
rectangle = Rectangle(5, 3)
print(f"Longueur: {rectangle.longueur}")     # 5
print(f"Aire: {rectangle.aire}")             # 15
print(f"Périmètre: {rectangle.perimetre}")   # 16