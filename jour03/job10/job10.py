def function(nb):
    if isinstance(nb , int) and nb >0 and nb %2==0:
        return "pair"
    elif isinstance(nb , int) and nb >0 and nb%2 != 0:
        return "impair"
    else:
        return "le nombre doit etre positif et entier"
            
var=function(2)
vari=function(3)
varia=function(3.5)
variab=function(-43)
print(var) 
print(vari)
print(varia)
print(variab)   