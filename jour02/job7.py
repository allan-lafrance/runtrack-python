def affiche_message(langage):
    if langage == "javascript":
        print("tu es un développeur web")
    elif langage == "python":
        print("tu es un développeur IA")
    elif langage == "java":
        print("tu es un développeur logiciel")
    elif langage == "reactjs":
        print("tu es un développeur mobile")
    else:
        print("un jour, je serai le meilleur développeur...")

affiche_message("javascript")  # imprimera "tu es un développeur web"
affiche_message("python")  # imprimera "tu es un développeur IA"
affiche_message("java")  # imprimera "tu es un développeur logiciel"
affiche_message("reactjs")  # imprimera "tu es un développeur mobile"
affiche_message("c++")  # imprimera "un jour, je serai le meilleur développeur..."