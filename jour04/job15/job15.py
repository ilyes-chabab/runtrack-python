import math

list=[22.4, 4.0, 16.22,9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
L=[]
for i in list:
    i=(math.floor(i))
    L.append(i)
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
tri_selection(L)
print(L)    