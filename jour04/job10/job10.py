L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

valeurs = [x for x in L if 25 <= x <= 90] #la variable "valeurs" sert a identifier les nombres qui se trouve entre 25 et 90

produit = 1
for valeur in valeurs:
    produit *= valeur

print(produit)
    