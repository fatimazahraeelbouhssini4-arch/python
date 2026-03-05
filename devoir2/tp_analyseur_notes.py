# ---------------------------------------------------------------------------
# DONNÉES FOURNIES
# ---------------------------------------------------------------------------

donnees = [
    ("Sara",    "Math",     12,    "G1"),
    ("Sara",    "Info",     14,    "G1"),
    ("Ahmed",   "Math",     9,     "G2"),
    ("Adam",    "Chimie",   18,    "G1"),
    ("Sara",    "Math",     11,    "G1"),
    ("Bouchra", "Info",     "abc", "G2"),
    ("",        "Math",     10,    "G1"),
    ("Yassine", "Info",     22,    "G2"),
    ("Ahmed",   "Info",     13,    "G2"),
    ("Adam",    "Math",     None,  "G1"),
    ("Sara",    "Chimie",   16,    "G1"),
    ("Adam",    "Info",     7,     "G1"),
    ("Ahmed",   "Math",     9,     "G2"),
    ("Hana",    "Physique", 15,    "G3"),
    ("Hana",    "Math",     8,     "G3"),
]

SEUIL_MOYENNE_FAIBLE = 10.0   # seuil pour alerte groupe
SEUIL_ECART_NOTES    = 10.0   # seuil d'écart min/max pour alerte instabilité


# =============================================================================
# PARTIE 1 : NETTOYAGE ET VALIDATION
# =============================================================================

def valider(enregistrement):
    """
    Valide un enregistrement (nom, matiere, note, groupe).
    Retourne (True, "") si valide, sinon (False, "raison : ...").
    """
    nom, matiere, note, groupe = enregistrement

    if not isinstance(nom, str) or nom.strip() == "":
        return (False, "raison : nom vide ou invalide")

    if not isinstance(matiere, str) or matiere.strip() == "":
        return (False, "raison : matière vide ou invalide")

    if not isinstance(groupe, str) or groupe.strip() == "":
        return (False, "raison : groupe vide ou invalide")

    if note is None:
        return (False, "raison : note manquante (None)")

    try:
        note_float = float(note)
    except (ValueError, TypeError):
        return (False, f"raison : note non numérique ('{note}')")

    if note_float < 0 or note_float > 20:
        return (False, f"raison : note hors plage [0,20] ({note_float})")

    return (True, "")


def nettoyer_donnees(donnees):
    """
    Divise les données en :
      - valides       : liste de tuples (nom, matiere, note_float, groupe)
      - erreurs       : liste de dicts {"ligne": ..., "raison": ...}
      - doublons_exact: set des tuples répétés exactement
    """
    valides        = []
    erreurs        = []
    doublons_exact = set()

    vus = {}   # tuple_original -> nb occurrences

    # Comptage des occurrences pour détecter les doublons exacts
    for enreg in donnees:
        vus[enreg] = vus.get(enreg, 0) + 1

    deja_ajoute_en_valides = set()

    for enreg in donnees:
        est_valide, raison = valider(enreg)

        if est_valide:
            nom, matiere, note, groupe = enreg
            tuple_nettoye = (nom.strip(), matiere.strip(), float(note), groupe.strip())

            # Détection doublon exact (même tuple original)
            if vus[enreg] > 1:
                doublons_exact.add(enreg)
                # N'ajouter qu'une seule fois dans valides
                if enreg not in deja_ajoute_en_valides:
                    valides.append(tuple_nettoye)
                    deja_ajoute_en_valides.add(enreg)
            else:
                valides.append(tuple_nettoye)
        else:
            erreurs.append({"ligne": enreg, "raison": raison})

    return valides, erreurs, doublons_exact


# =============================================================================
# PARTIE 2 : STRUCTURATION
# =============================================================================

def extraire_matieres(valides):
    """
    Retourne un set de toutes les matières distinctes.
    """
    matieres = set()
    for _, matiere, _, _ in valides:
        matieres.add(matiere)
    return matieres


def construire_notes_par_etudiant(valides):
    """
    Retourne un dict :  { nom: { matiere: [note, ...] } }
    """
    notes_par_etudiant = {}
    for nom, matiere, note, _ in valides:
        if nom not in notes_par_etudiant:
            notes_par_etudiant[nom] = {}
        if matiere not in notes_par_etudiant[nom]:
            notes_par_etudiant[nom][matiere] = []
        notes_par_etudiant[nom][matiere].append(note)
    return notes_par_etudiant


def construire_groupes(valides):
    """
    Retourne un dict : { groupe: set(noms) }
    """
    groupes = {}
    for nom, _, _, groupe in valides:
        if groupe not in groupes:
            groupes[groupe] = set()
        groupes[groupe].add(nom)
    return groupes


# =============================================================================
# PARTIE 3 : CALCULS ET STATISTIQUES (récursivité)
# =============================================================================

def somme_recursive(liste, index=0):
    """
    Calcule la somme d'une liste de nombres par récursivité.
    """
    if index == len(liste):
        return 0
    return liste[index] + somme_recursive(liste, index + 1)


def moyenne(liste):
    """
    Calcule la moyenne d'une liste (utilise somme_recursive).
    Retourne None si la liste est vide.
    """
    if len(liste) == 0:
        return None
    return somme_recursive(liste) / len(liste)


def calculer_statistiques(notes_par_etudiant):
    """
    Retourne un dict :
      {
        nom: {
          "moyenne_generale": float,
          "moyennes_par_matiere": { matiere: float }
        }
      }
    """
    stats = {}
    for nom, matieres_notes in notes_par_etudiant.items():
        moyennes_par_matiere = {}
        toutes_les_notes = []

        for matiere, notes in matieres_notes.items():
            moy = moyenne(notes)
            moyennes_par_matiere[matiere] = moy
            toutes_les_notes.extend(notes)

        stats[nom] = {
            "moyenne_generale":    moyenne(toutes_les_notes),
            "moyennes_par_matiere": moyennes_par_matiere
        }
    return stats


# =============================================================================
# PARTIE 4 : ANALYSE AVANCÉE ET DÉTECTION D'ANOMALIES
# =============================================================================

def detecter_anomalies(notes_par_etudiant, groupes, stats,
                       seuil_faible=SEUIL_MOYENNE_FAIBLE,
                       seuil_ecart=SEUIL_ECART_NOTES):
    """
    Détecte 4 types d'anomalies et les regroupe dans un dict d'alertes :
      {
        "notes_multiples"   : [ {"etudiant": ..., "matiere": ..., "notes": ...} ],
        "profil_incomplet"  : [ {"etudiant": ..., "matieres_manquantes": ...} ],
        "groupe_faible"     : [ {"groupe": ..., "moyenne": ...} ],
        "ecart_eleve"       : [ {"etudiant": ..., "note_min": ..., "note_max": ..., "ecart": ...} ]
      }
    """
    alertes = {
        "notes_multiples":  [],
        "profil_incomplet": [],
        "groupe_faible":    [],
        "ecart_eleve":      []
    }

    # Ensemble de toutes les matières connues
    toutes_matieres = set()
    for matieres_notes in notes_par_etudiant.values():
        toutes_matieres.update(matieres_notes.keys())

    # --- Anomalie 1 : plusieurs notes pour une même matière ---
    for nom, matieres_notes in notes_par_etudiant.items():
        for matiere, notes in matieres_notes.items():
            if len(notes) > 1:
                alertes["notes_multiples"].append({
                    "etudiant": nom,
                    "matiere":  matiere,
                    "notes":    notes
                })

    # --- Anomalie 2 : profil incomplet ---
    for nom, matieres_notes in notes_par_etudiant.items():
        matieres_etudiant   = set(matieres_notes.keys())
        matieres_manquantes = toutes_matieres - matieres_etudiant
        if matieres_manquantes:
            alertes["profil_incomplet"].append({
                "etudiant":            nom,
                "matieres_manquantes": matieres_manquantes
            })

    # --- Anomalie 3 : groupe à moyenne faible ---
    for groupe, membres in groupes.items():
        notes_groupe = []
        for nom in membres:
            if nom in stats and stats[nom]["moyenne_generale"] is not None:
                notes_groupe.append(stats[nom]["moyenne_generale"])
        if notes_groupe:
            moy_groupe = moyenne(notes_groupe)
            if moy_groupe is not None and moy_groupe < seuil_faible:
                alertes["groupe_faible"].append({
                    "groupe":  groupe,
                    "moyenne": round(moy_groupe, 2)
                })

    # --- Anomalie 4 : écart important entre note min et max ---
    for nom, matieres_notes in notes_par_etudiant.items():
        toutes_notes = []
        for notes in matieres_notes.values():
            toutes_notes.extend(notes)
        if len(toutes_notes) >= 2:
            note_min = min(toutes_notes)
            note_max = max(toutes_notes)
            ecart    = note_max - note_min
            if ecart >= seuil_ecart:
                alertes["ecart_eleve"].append({
                    "etudiant": nom,
                    "note_min": note_min,
                    "note_max": note_max,
                    "ecart":    ecart
                })

    return alertes


# =============================================================================
# AFFICHAGE DES RÉSULTATS
# =============================================================================

def afficher_separateur(titre):
    print("\n" + "=" * 65)
    print(f"  {titre}")
    print("=" * 65)


def afficher_resultats(valides, erreurs, doublons_exact,
                       matieres, notes_par_etudiant, groupes,
                       stats, alertes):

    # ── Partie 1 ────────────────────────────────────────────────
    afficher_separateur("PARTIE 1 — NETTOYAGE ET VALIDATION")

    print(f"\n  Enregistrements valides ({len(valides)}) :")
    for v in valides:
        print(f"    {v}")

    print(f"\n  Erreurs détectées ({len(erreurs)}) :")
    for e in erreurs:
        print(f"    Ligne  : {e['ligne']}")
        print(f"    Erreur : {e['raison']}")
        print()

    print(f" Doublons exacts ({len(doublons_exact)}) :")
    for d in doublons_exact:
        print(f"    {d}")

    # ── Partie 2 ────────────────────────────────────────────────
    afficher_separateur("PARTIE 2 — STRUCTURATION")

    print(f"\n Matières distinctes : {matieres}")

    print("\n  Notes par étudiant (hiérarchie) :")
    for nom, matieres_notes in notes_par_etudiant.items():
        print(f"    {nom} :")
        for mat, notes in matieres_notes.items():
            print(f"      └─ {mat} : {notes}")

    print("\n  Groupes pédagogiques :")
    for groupe, membres in groupes.items():
        print(f"    {groupe} : {membres}")

    # ── Partie 3 ────────────────────────────────────────────────
    afficher_separateur("PARTIE 3 — CALCULS ET STATISTIQUES")

    print("\n Statistiques par étudiant :")
    for nom, s in stats.items():
        moy_gen = round(s["moyenne_generale"], 2) if s["moyenne_generale"] is not None else "N/A"
        print(f"\n    {nom}  —  Moyenne générale : {moy_gen}")
        for mat, moy in s["moyennes_par_matiere"].items():
            moy_affiche = round(moy, 2) if moy is not None else "N/A"
            print(f"      └─ {mat} : {moy_affiche}")

    # ── Partie 4 ────────────────────────────────────────────────
    afficher_separateur("PARTIE 4 — ANOMALIES DÉTECTÉES")

    print("\n  Notes multiples pour une même matière :")
    if alertes["notes_multiples"]:
        for a in alertes["notes_multiples"]:
            print(f"    {a['etudiant']} / {a['matiere']} → notes : {a['notes']}")
    else:
        print("    Aucune anomalie.")

    print("\n  Profils incomplets (matières manquantes) :")
    if alertes["profil_incomplet"]:
        for a in alertes["profil_incomplet"]:
            print(f"    {a['etudiant']} → manquantes : {a['matieres_manquantes']}")
    else:
        print("    Aucune anomalie.")

    print(f"\n  Groupes à moyenne faible (< {SEUIL_MOYENNE_FAIBLE}) :")
    if alertes["groupe_faible"]:
        for a in alertes["groupe_faible"]:
            print(f"    {a['groupe']} → moyenne : {a['moyenne']}")
    else:
        print("    Aucune anomalie.")

    print(f"\n  Étudiants avec écart élevé entre notes (≥ {SEUIL_ECART_NOTES}) :")
    if alertes["ecart_eleve"]:
        for a in alertes["ecart_eleve"]:
            print(f"    {a['etudiant']} → min={a['note_min']}  max={a['note_max']}  écart={a['ecart']}")
    else:
        print("    Aucune anomalie.")

    print("\n" + "=" * 65)
    print("  FIN DE L'ANALYSE")
    print("=" * 65 + "\n")


# =============================================================================
# PROGRAMME PRINCIPAL
# =============================================================================

if __name__ == "__main__":

    # ── Partie 1 ──
    valides, erreurs, doublons_exact = nettoyer_donnees(donnees)

    # ── Partie 2 ──
    matieres           = extraire_matieres(valides)
    notes_par_etudiant = construire_notes_par_etudiant(valides)
    groupes            = construire_groupes(valides)

    # ── Partie 3 ──
    stats = calculer_statistiques(notes_par_etudiant)

    # ── Partie 4 ──
    alertes = detecter_anomalies(notes_par_etudiant, groupes, stats)

    # ── Affichage ──
    afficher_resultats(valides, erreurs, doublons_exact,
                       matieres, notes_par_etudiant, groupes,
                       stats, alertes)