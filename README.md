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
└── README.md
```

---

## Exécution

```bash
# Devoir 1
python devoir1/ex1.py

# Devoir 2
python devoir2/tp_analyseur_notes.py
```

> Nécessite Python 3.x — aucune bibliothèque externe requise.
