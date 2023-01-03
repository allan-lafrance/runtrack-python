def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Opérateur non valide"

resultat = calcule(1, "+", 2)  # retournera 3
resultat = calcule(3, "-", 4)  # retournera -1
resultat = calcule(5, "*", 6)  # retournera 30
resultat = calcule(7, "/", 8)  # retournera 0.875
resultat = calcule(9, "%", 10)  # retournera 9
resultat = calcule(11, "^", 12)  # retournera "Opérateur non valide"