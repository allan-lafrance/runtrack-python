L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

maxi = L[0]
mini = L[0]

for nombre in L:
    if nombre > maxi:
        maxi = nombre
    if nombre < mini:
        mini = nombre

print(f"Le maximum de la liste est {maxi} et le minimum est {mini}.")