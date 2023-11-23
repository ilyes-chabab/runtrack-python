def function():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    maxi= None
    mini= None
    for i in L:
        if maxi is None or i > maxi:
            maxi = i
    for i in L:
        if mini is None or i < mini:
            mini = i                          
    print(f"la valeur minimale est : {maxi}")                        
    print(f"la valeur minimale est : {mini}")
 
var=function()
print(var)          
