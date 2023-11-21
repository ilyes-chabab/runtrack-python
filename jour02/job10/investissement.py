montant=int(input("quel est le montant de votre investissement ? : "))
tx_de_rendement=int(input("quel est le taux de rendement ? : "))
gain_annuel=montant+(montant*tx_de_rendement/100)
print("votre gain annuel sera de" , gain_annuel , "€")
montant=int(montant) + 5000
tx_de_rendement=int(tx_de_rendement) +2
gain_annuel=montant+(montant*tx_de_rendement/100)
print("Vous avez ajouté 5000€ à votre capital et suite a ça , le taux de rendement a augmenté de 2%.")
print("Votre nouveau gain annuel actuel est de : ",gain_annuel,"€")
montant=int(montant)-(int(montant)*abs(-10)/100)
tx_de_rendement=int(tx_de_rendement)-1
gain_annuel=montant+(montant*tx_de_rendement/100)
print("vous avez decidé de retirer 10% de votre montant,")
print("votre investissement s'eleve maintenant a ",montant,"€")
print("suite a ça le taux de rendement a diminué de 1%")
print("le nouveau gain annuel est de ",gain_annuel,"€")