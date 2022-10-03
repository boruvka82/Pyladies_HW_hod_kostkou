from random import randrange

def hod_kostkou(hrac):
    """bude vracet počet pokusů než hráči padla šestka."""
    
    pocet_hodu_hrac = 0     
    
    while True:
        hod = randrange(1,7)
        pocet_hodu_hrac = pocet_hodu_hrac + 1   
        print("hrac", hrac, "hodil", hod) 
        if hod==6:
            print("celkem", pocet_hodu_hrac)
            print()
            break  
    return pocet_hodu_hrac

maximum = 0

for hrac in range(1,5):
    celkem_hodu = hod_kostkou(hrac)
    if maximum < celkem_hodu:
        maximum = celkem_hodu
        vitez = hrac

print("vitez je hrac",vitez,"s maximem hodu:",maximum) 
