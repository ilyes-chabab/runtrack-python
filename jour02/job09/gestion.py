nom="chat"
prix_unitaire=50
inflation=10
nouveau_prix_unitaire=prix_unitaire +(prix_unitaire*inflation/100)
quantité_en_stock=100
print("produit :",nom)
print("prix : ",nouveau_prix_unitaire,"€ (prix après inflation)")
print("stock restant : ",quantité_en_stock)
ajout_de_stock= int(input("combien de produit voulez vous ajouter au stock ? : "))
quantité_en_stock += ajout_de_stock
print("il y a" ,quantité_en_stock,"chat(s)")
achat= int(input("combien de chats voulez vous acheter ? : "))
if int(achat) > int(quantité_en_stock):
    print("ce n'est pas possible , il n'y a pas assez de chats")
else:   
    quantité_en_stock -= achat
    print("il reste" , quantité_en_stock ,"chat(s)")
