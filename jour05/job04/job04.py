n=1
n= n + int(input("quel longeur voulez-vous ? : "))
ligne="+"+n*"-"+"+"
print(ligne)
for _ in range(n):
    debut= n
    fin=n-n
    for _ in range(debut):
        if debut==0:
            break
        else:           
            debut= debut -1
            print("|"+debut*"#"+" "+fin*"#" +"|")
            fin = fin +1 
        # while debut >0:
        #     debut= debut -1
        #     print("|"+debut*"#"+" "+fin*"#" +"|")
        #     fin = fin +1 
        #     break
print(ligne)          
   