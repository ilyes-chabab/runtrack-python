def draw_rectangle(width,height):
    haut_bas = "|"+(width -2)*"-"+"|"
    print(haut_bas)
    for i in range(height-2):
        cotés="|"+(width -2)*" "+"|"   
        print(cotés)  
    print(haut_bas)    

draw_rectangle(10,3)    