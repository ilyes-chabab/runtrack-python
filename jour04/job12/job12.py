def tri_selection(liste):
    i = 0
    while True:
        try:
            liste[i]
            i += 1
        except IndexError:
            break
    i -= 1  
    while i > 0:
        indice_max = 0
        j = 1
        while j <= i:
            if liste[j] > liste[indice_max]:
                indice_max = j
            j += 1        
        liste[i], liste[indice_max] = liste[indice_max], liste[i]
        i -= 1
list = [30, 10, 20, 50, 40]
tri_selection(list)
print(list)
         