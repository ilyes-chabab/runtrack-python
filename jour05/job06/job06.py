def function(nb_marche , marche_en_cm):
    metre=((nb_marche*marche_en_cm)*5)*7
    return metre

print(f"Pour x marches de y cm, le gardien parcourt {function(10,10)}m par semaine.")

