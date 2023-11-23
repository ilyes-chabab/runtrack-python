
def time_to_text(minute):
    heure=minute//60
    min=minute%60
    hm=(f"{heure}heures et {min} minutes")
    return hm    
    
temps=time_to_text(70)
print(temps)       