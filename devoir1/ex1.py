age = int(input("Veuillez entrer votre âge : "))

if age <= 12:
    print("Vous êtes un enfant (0-12 ans).")
elif age <= 17:
    print("Vous êtes un adolescent (13-17 ans).")
elif age <= 64:
    print("Vous êtes un adulte (18-64 ans).")
else:
    print("Vous êtes un senior (65 ans et plus).")