def affiche_signe(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")

affiche_signe(1)  # imprimera "positif"
affiche_signe(-1)  # imprimera "négatif"
affiche_signe(0)  # ne imprimera rien