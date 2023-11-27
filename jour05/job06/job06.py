def function(nb_marche , marche_en_cm):
    metre=(((nb_marche*marche_en_cm)*5)*7)*2 # 5fois par jours 7 jours dans la semaine 2fois pour la descente et la remonté 
    return metre
nb_marche=10
marche_en_cm=10

print(f"Pour {nb_marche} marches de {marche_en_cm} cm, le gardien parcourt {function(nb_marche,marche_en_cm)}m par semaine.")

