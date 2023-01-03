def affiche_fruits_legumes(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "légumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légumes" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("type ou saison non reconnu")

affiche_fruits_legumes("fruits", "hiver")  # imprimera "orange, mandarine et kiwi"
affiche_fruits_legumes("fruits", "été")  # imprimera "poire, fraise, cassis"
affiche_fruits_legumes("légumes",