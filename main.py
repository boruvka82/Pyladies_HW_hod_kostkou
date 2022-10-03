def hod_kostkou():
   """bude vracet počet pokusů než hráči padla šestka"""

from random import randrange


vitez = 0
maximum = 0
for hrac in range(1,5):
    
    #number = int(input("zadej cislo: "))
    pocet_hodu_hrac = 0  
    while True:
         
        hod = randrange(1,7)
        pocet_hodu_hrac = pocet_hodu_hrac + 1 
        print("hrac",hrac, "hodil", hod) 
        if hod==6:
            print() 
            break
            
    if pocet_hodu_hrac > maximum:
        maximum = pocet_hodu_hrac
        vitez = hrac
print("vitez hrac",vitez,"maximum",maximum)    
