# =========================
# Données (liste de tuples)
# =========================
donnees = [
    ("Sara", "Math", 12, "G1"),
    ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"),
    ("Bouchra", "Info", "abc", "G2"),  # erreur : note non numérique
    ("", "Math", 10, "G1"),            # erreur : nom vide
    ("Yassine", "Info", 22, "G2"),     # erreur : note > 20
    ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"),      # erreur : note vide
    ("Sara", "Chimie", 16, "G1"),
    ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"),        # doublon
    ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3"),
]

# =========================
# PARTIE 1 : Validation
# =========================

def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement

    if not nom:
        return False, "nom vide"

    if not matiere:
        return False, "matière vide"

    if not groupe:
        return False, "groupe vide"

    if not isinstance(note, (int, float)):
        return False, "note non numérique"

    if note < 0 or note > 20:
        return False, "note hors intervalle"

    return True, ""

valides = []
erreurs = []
vus = set()
doublons_exact = set()

for ligne in donnees:

    # détection des doublons
    if ligne in vus:
        doublons_exact.add(ligne)
    else:
        vus.add(ligne)

    # validation
    ok, raison = valider(ligne)

    if ok:
        nom, matiere, note, groupe = ligne
        valides.append((nom, matiere, float(note), groupe))
    else:
        erreurs.append({"ligne": ligne, "raison": raison})

# =========================
# PARTIE 2 : Structuration
# =========================

matieres = set()
for _, matiere, _, _ in valides:
    matieres.add(matiere)

etudiants = {}

for nom, matiere, note, groupe in valides:

    if nom not in etudiants:
        etudiants[nom] = {}

    if matiere not in etudiants[nom]:
        etudiants[nom][matiere] = []

    etudiants[nom][matiere].append(note)

groupes = {}

for nom, matiere, note, groupe in valides:

    if groupe not in groupes:
        groupes[groupe] = set()

    groupes[groupe].add(nom)

# =========================
# PARTIE 3 : Calculs
# =========================

def somme_recursive(liste):
    if len(liste) == 0:
        return 0
    return liste[0] + somme_recursive(liste[1:])

def moyenne(liste):
    if len(liste) == 0:
        return 0
    return somme_recursive(liste) / len(liste)

moyennes_etudiants = {}

for nom in etudiants:
    toutes_notes = []

    for mat in etudiants[nom]:
        toutes_notes += etudiants[nom][mat]

    moyennes_etudiants[nom] = moyenne(toutes_notes)

moyennes_matieres = {}

for mat in matieres:
    notes = []

    for nom in etudiants:
        if mat in etudiants[nom]:
            notes += etudiants[nom][mat]

    moyennes_matieres[mat] = moyenne(notes)

# =========================
# PARTIE 4 : Analyse
# =========================

alertes = []

# doublons matière
for nom in etudiants:
    for mat in etudiants[nom]:
        if len(etudiants[nom][mat]) > 1:
            alertes.append({
                "type": "doublon matière",
                "etudiant": nom,
                "matiere": mat
            })

# profils incomplets
for nom in etudiants:
    if len(etudiants[nom]) < len(matieres):
        alertes.append({
            "type": "profil incomplet",
            "etudiant": nom
        })

# groupes faibles
seuil = 10

for g in groupes:
    notes = []

    for nom in groupes[g]:
        notes.append(moyennes_etudiants[nom])

    if moyenne(notes) < seuil:
        alertes.append({
            "type": "groupe faible",
            "groupe": g
        })

# écarts élevés
for nom in etudiants:
    notes = []

    for mat in etudiants[nom]:
        notes += etudiants[nom][mat]

    if notes and (max(notes) - min(notes) > 10):
        alertes.append({
            "type": "écart élevé",
            "etudiant": nom
        })

# =========================
# Affichage
# =========================

print("Valides :", valides)
print("Erreurs :", erreurs)
print("Doublons :", doublons_exact)
print("Matières :", matieres)
print("Moyennes étudiants :", moyennes_etudiants)
print("Moyennes matières :", moyennes_matieres)
print("Alertes :", alertes)
