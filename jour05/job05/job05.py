# phrase=input("quelle est votre phrase ? : ")
def function(message):
    phrase_decaler=""
    for i in message:
        majuscule=i.isupper() #isupper trouve les lettre majuscule
        i= i.lower() #.lower sert a rendre les lettres majuscule en minuscule pour faciliter le decalage
        decale= (ord(i) - ord("a") + 3) %26
        lettre_decaler= chr(decale + ord("a"))
        if majuscule:
            lettre_decaler= lettre_decaler.upper()

    return phrase_decaler    

phrase=input("quelle est votre phrase ? : ")
function(phrase)


# i="A"
# L=[]
# i = ord(i)+3
# L.append(chr(i))   
# print(L)



