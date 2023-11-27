list=[38,80, 81, 82,83 ,84 ,85 ,86 ,87 ,88, 89, 90] 
liste_arrondie=[]
def function():
    for note in list:
        if note<40:
            note=note
        elif (note +1) %5 ==0:
            note= note+1
        elif (note +2) %5 ==0:
            note=note +2
        else:
            note=note
        liste_arrondie.append(note)        
    return liste_arrondie
var=function()
print(var)