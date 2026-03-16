class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age

    def se_presenter(self):
        return f"Je suis {self._nom}, {self._age} ans"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("Entrez une valeur INT!")
        if valeur < 0:
            raise ValueError("La valeur ne peut pas être moins que 0")
        if valeur > 140:
            raise ValueError("L'âge ici est irréaliste")
        self._age = valeur

# Utilisation
personne1 = Personne("Sara", 25)
personne2 = Personne("Ahmed", 18)
personne3 = Personne("Med", 32)

print(personne1.se_presenter())  # Je suis Sara, 25 ans
personne1.age = 26               # OK
personne1.age = -5               # ValueError: La valeur ne peut pas être moins que 0
personne1.age = 200              # ValueError: L'âge ici est irréaliste
personne1.age = "vingt"          # TypeError: Entrez une valeur INT!