def draw_rectangle(width,height):
    haut = "|"+width*"-"+"|"
    print(haut)
    for _ in range(height-2):
        cotés="|"+width*" "+"|"   
        print(cotés)  
    print(haut)    

draw_rectangle(11,4)    