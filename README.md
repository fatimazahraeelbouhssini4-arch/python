# Python & Django — Travaux Pratiques

**Nom :** Fatima Zahra Elbouhssini
**Filière :** Bachelor IDAI
**Année :** 2025/2026

---

## 📌 Description

Ce dépôt contient l’ensemble des travaux pratiques réalisés dans le cadre du module Python et développement web avec Django.

Il regroupe :

* les bases de Python
* un projet d’analyse de données
* la programmation orientée objet (POO)
* un projet web avec Django

---

# 🧩 Partie 1 — Python

## 🔹 Devoir 1 : Les bases de Python

**Dossier :** `devoir1/`
**Description :** Exercices sur les bases de Python : conditions, boucles, listes et interaction utilisateur.

| Fichier  | Description               | Notions utilisées   |
| -------- | ------------------------- | ------------------- |
| `ex1.py` | Contrôle d'âge            | `input()`, `if`     |
| `ex2.py` | Carnet d'adresses         | `while`, `append()` |
| `ex3.py` | Vérification mot de passe | boucle `while`      |
| `ex4.py` | Calculatrice              | conditions          |

---

## 🔹 Devoir 2 : Analyseur de notes

**Dossier :** `devoir2/`

**Description :** Application Python pour analyser des notes étudiantes.

### Fonctionnalités :

* Nettoyage des données
* Organisation des informations
* Calcul des moyennes
* Détection d’anomalies

### Notions utilisées :

* `list`, `dict`, `set`, `tuple`
* fonctions
* récursivité

---

## 🔹 Devoir 3 : Programmation Orientée Objet (POO)

**Dossier :** `devoir3/`

**Description :** Exercices sur les concepts fondamentaux de la POO.

| Fichier | Notions           |
| ------- | ----------------- |
| `21.py` | Classes et objets |
| `22.py` | Attributs         |
| `29.py` | Encapsulation     |
| `32.py` | Properties        |
| `33.py` | Héritage          |
| `35.py` | Polymorphisme     |
| `36.py` | Héritage multiple |

---

# 🌐 Partie 2 — TP Django

## 🔹 Description

Ce projet consiste à créer une application web avec Django en respectant l’architecture MVT (Model - View - Template).

---

## ⚙️ Étapes réalisées

### ✔️ Installation

* Installation de Python
* Installation de Django avec pip

### ✔️ Environnement virtuel

Création et activation d’un environnement virtuel pour isoler les dépendances.

### ✔️ Création du projet

```bash
django-admin startproject myproject
```

### ✔️ Création d’une application

```bash
python manage.py startapp myapp
```

---

## 🏗️ Structure du projet Django

```
myproject/
│
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── admin.py
```

---

## 🔄 Fonctionnement Django (MVT)

* **Model** : gère la base de données
* **View** : contient la logique
* **Template** : affiche les pages HTML

---

## 🌍 Fonctionnalités réalisées

* Création de pages web avec templates
* Gestion des URLs
* Formulaire (compteur de mots)
* Intégration de Bootstrap
* Gestion des fichiers statiques (CSS, JS)
* Création de modèles et migrations
* Interface d’administration Django
* Authentification (inscription, connexion, déconnexion)

---

## ▶️ Lancer le projet Django

```bash
cd myproject
python manage.py runserver
```

Puis ouvrir :

```
http://127.0.0.1:8000/
```

---

# 📂 Structure globale du dépôt

```
python/
├── devoir1/
├── devoir2/
├── devoir3/
├── myproject/
├── myapp/
└── README.md
```

---

# ▶️ Exécution

```bash
# Devoir 1
python devoir1/ex1.py

# Devoir 2
python devoir2/tp_analyseur_notes.py

# Devoir 3
python devoir3/21.py

# Django
python manage.py runserver
```

---

## ✅ Remarque

* Python 3.x requis
* Django installé via pip
* Aucun autre module externe nécessaire

---

## 🎯 Conclusion

Ce dépôt regroupe les compétences acquises en Python et en développement web avec Django, notamment la programmation structurée, la POO et la création d’applications web complètes.
