def moyenne(note1,note2,note3):   
    return ((float(note1)+float(note2)+float(note3))/3)
note1=float(input("quelle est votre premiere note : "))
note2=float(input("quelle est votre deuxieme note : "))
note3=float(input("quelle est votre troisieme note : "))
moyenne_etudiant=moyenne(note1,note2,note3)
if moyenne_etudiant <=20 and moyenne_etudiant>=15:
    print(f"{moyenne_etudiant} ,Très bon élève !")
elif moyenne_etudiant <15 and moyenne_etudiant>=11:
    print(f"{moyenne_etudiant} ,bon élève !")
elif moyenne_etudiant <11 and moyenne_etudiant>=8:
    print(f"{moyenne_etudiant} ,élève moyen .")
elif moyenne_etudiant <8 and moyenne_etudiant>=0:
    print(f"{moyenne_etudiant} ,élève devant faire des efforts...")           
