n=int(input("entrez un nombre supérieur à 0 : ")) #création de la variable n (écrite par l'utilisateur)
for i in range(1 ,n+1):
    print(f"table de multiplication de {i}: ")
    for a in range(1,11): # a est la variable des nombre multiplicateur de 1 à 10
        resultat= i*a
        print(f"{i} * {a} = {resultat}")