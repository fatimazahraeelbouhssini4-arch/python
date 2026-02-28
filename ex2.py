
contacts = ["Bouchra", "Ahmed", "Sara"]

while True:
    print("\n=== CARNET D'ADRESSES ===")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter")

    choix = input("\nVotre choix : ")

    if choix == "1":
        # Saisie et ajout avec .append()
        nom = input("Entrez le nom du contact : ")
        contacts.append(nom)
        print("Contact ajouté avec succès.")

    elif choix == "2":
        # Affichage avec enumerate()
        print("\n--- Liste des contacts ---")
        for index, contact in enumerate(contacts, start=1):
            print(index, "-", contact)

    elif choix == "3":
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
