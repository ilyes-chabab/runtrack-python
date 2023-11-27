def decale_message(message):
    message_decale = ''
    for lettre in message:
        # Vérifier si le caractère est une lettre de l'alphabet
        if lettre.isalpha():
            # Convertir en minuscule pour simplifier les opérations
            est_majuscule = lettre.isupper()
            lettre = lettre.lower()
            # Calculer le décalage en prenant en compte le dépassement
            decalage_reel = (ord(lettre) - ord('a') + 3) % 26
            # Convertir le caractère décalé
            lettre_decalee = chr(decalage_reel + ord('a'))
            # Reconvertir en majuscule si nécessaire
            if est_majuscule:
                lettre_decalee = lettre_decalee.upper()
            # Ajouter la lettre décalée au message
            message_decale += lettre_decalee
        else:
            # Si ce n'est pas une lettre, ajouter directement au message
            message_decale += lettre

    return message_decale

# Exemple d'utilisation de la fonction
message_original = "Bonjour XYZ !"
message_decale = decale_message(message_original)
print( message_decale)


