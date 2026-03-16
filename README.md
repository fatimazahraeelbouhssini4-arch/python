# Python — Travaux Pratiques
**Nom :** Fatima Zahra Elbouhssini  
**Filière :** Bachelor IDAI  
**Date :** Février 2026

---

## Description
Ce dépôt contient les devoirs réalisés dans le cadre du cours de Python.
Chaque devoir est organisé dans un dossier séparé.

---

## Devoir 1 - Les bases de Python
**Dossier :** `devoir1/`  
**Description :** 4 exercices sur les bases de Python : saisie utilisateur, conditions, boucles et listes.

| Fichier | Description | Notions utilisées |
|--------|-------------|-------------------|
| `ex1.py` | Contrôle d'âge : affiche la catégorie selon l'âge saisi | `input()`, `int()`, `if / elif / else` |
| `ex2.py` | Carnet d'adresses : menu interactif pour gérer des contacts | `while`, `append()`, `enumerate()` |
| `ex3.py` | Mot de passe : redemande tant que la saisie est incorrecte | `while`, `input()`, comparaison de chaînes |
| `ex4.py` | Calculatrice : opérations de base avec gestion division par zéro | `float()`, `if / elif / else` |

---

## Devoir 2 - Analyseur de notes et cohérence pédagogique
**Dossier :** `devoir2/`  
**Description :** Programme complet d'analyse de données étudiantes en 4 parties.

| Fichier | Description | Notions utilisées |
|--------|-------------|-------------------|
| `tp_analyseur_notes.py` | Nettoyage, structuration, statistiques et détection d'anomalies sur des notes | `list`, `dict`, `set`, `tuple`, récursivité |

**Détail des parties :**
- **Partie 1 :** Validation et nettoyage des données (erreurs, doublons)
- **Partie 2 :** Structuration hiérarchique (matières, notes par étudiant, groupes)
- **Partie 3 :** Calcul de moyennes avec une fonction récursive
- **Partie 4 :** Détection d'anomalies (notes multiples, profil incomplet, groupe faible, écart élevé)

---

## Devoir 3 - Programmation Orientée Objet (POO)
**Dossier :** `devoir3/`  
**Description :** Exercices sur les concepts fondamentaux de la POO en Python.

| Fichier | Description | Notions utilisées |
|--------|-------------|-------------------|
| `21.py` | Création de classes et instances | `class`, `__init__`, `self` |
| `22.py` | Attributs publics et protégés | `_attribut`, notation pointée |
| `29.py` | Encapsulation et attributs privés | `__attribut`, getter, setter |
| `32.py` | Properties et validation | `@property`, `@setter`, `isinstance` |
| `33.py` | Héritage simple | `super()`, surcharge de méthodes |
| `35.py` | Polymorphisme | méthodes surchargées, boucle sur objets |
| `36.py` | Héritage multiple | `class Fille(Mere1, Mere2)` |

---

## Structure du dépôt
```
python/
├── devoir1/
│   ├── ex1.py
│   ├── ex2.py
│   ├── ex3.py
│   ├── ex4.py
│   └── README.md
├── devoir2/
│   ├── tp_analyseur_notes.py
│   └── README.md
├── devoir3/
│   ├── 21.py
│   ├── 22.py
│   ├── 29.py
│   ├── 32.py
│   ├── 33.py
│   ├── 35.py
│   ├── 36.py
│   └── README.md
└── README.md
```

---

## Exécution
```bash
# Devoir 1
python devoir1/ex1.py

# Devoir 2
python devoir2/tp_analyseur_notes.py

# Devoir 3
python devoir3/21.py
```

> Nécessite Python 3.x — aucune bibliothèque externe requise.
