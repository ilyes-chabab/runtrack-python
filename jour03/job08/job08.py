def function(type,saison):
    if type == str("fruits") and saison == str("hiver"):
        return "orange , mandarine et kiwi"
    if type == str("fruits") and saison == str("ete"):
        return "Poire, fraise, cassis"
    if type == str("legume") and saison == str("hiver"):
        return "carotte, topinambour, endive"
    if type == str("legume") and saison == str("ete"):
        return "artichaut, aubergine,navet"
variable=function("legume","ete")
print(variable)