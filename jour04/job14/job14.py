def my_long_word(longueur, phrase):
    mots = []
    mot_actuel = ""
    resultat = ""
    for caractere in phrase:
        if caractere != " ":
            mot_actuel += caractere
        else:
            if mot_actuel != "":
                mots.append(mot_actuel)
                mot_actuel = ""
    for mot in mots:
        nb_caracteres = 0
        for _ in mot:
            nb_caracteres += 1
        
        if nb_caracteres > longueur:
            resultat += mot + " "

    return resultat


resultat = my_long_word(3,"peur chemin vers côté obscur peur mène colère colère mène haine haine mène souffrance ")
print(resultat)