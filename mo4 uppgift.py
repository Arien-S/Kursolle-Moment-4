#Moment 04
#Importerar moduler
import sys

import time

#Gör en funktion till menyn som startar funktioner baserat på input
def start():
    time.sleep(0.5)
    print("Välkommen till menyn!")
    time.sleep(1.5)
    print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")
    time.sleep(2)
    program = str(input("Vill du räkna ut area eller omkrets?"))
    
    if ("omkrets") in program:
        print("Då kör vi!")
        Räknare_O()
    
    elif ("area") in program:
        print("Då kör vi!")
        Räknare_A()

#Gör en funktion för omkrets räknaren
def Räknare_O():
    
    try:
        sida_1 = int(input("Ange ena sidan på din figur"))
        
    except ValueError:
        print("Du får endast skriva heltal")
        sida_1 = int(input("Ange ena sidan på din figur"))
            

    try:
        sida_2 = int(input("Ange andra sidan på din figur"))
        
    except ValueError:
        print("Du får endast skriva heltal")
        sida_2 = int(input("Ange andra sidan på din figur"))
        
    omkrets = (sida_1+sida_2)*2
    
    print(f"Omkretsen på din rektangel med sidorna {sida_1} och {sida_2} är = {omkrets}")
        
    
    
    
#Gör en funktion för Area räknaren
def Räknare_A():

#Gör så att man endast får skriva heltal annars får man börja om
    try:
        sida_1 = int(input("Ange ena sidan på din figur"))
        
    except ValueError:
        print("Du får endast skriva heltal")
        sida_1 = int(input("Ange ena sidan på din figur"))
            

    try:
        sida_2 = int(input("Ange andra sidan på din figur"))
        
    except ValueError:
        print("Du får endast skriva heltal")
        sida_2 = int(input("Ange andra sidan på din figur"))
            
#Printar vilken figure det är beroende på värdet man skriver in   
    if sida_1 == sida_2:
        print("Detta är en kvadrat")
            
    elif sida_1 != sida_2:
        print("Detta är en rektangel")
        
#gör samma sak som förra try excepten           
    try:
        höjd = int(input("Ange figurens höjd"))
            
    except ValueError:
        print("Du får endast skriva heltal")
        höjd = int(input("Ange figurens höjd"))
#ALla höjder under noll blir 1 och alla över 10 blir 10
    if höjd < 0:
        höjd = 1
        
    elif höjd > 10:
        höjd = 10
        
#Definerar variabel för hur arean beräknas    
    area = sida_1*sida_2

    time.sleep(1)
    print(f"Med dina angivna mått blir arean på din geometriska form {area}")
    time.sleep(1)
    print("Här är vad volymen blir beroende på olika höjder")
    time.sleep(1)
    print("Höjd  |  Volym\n--------------")
#Printar volymen beroende på olika höjder med foor loop
    for i in range(1,höjd+1):
        time.sleep(1)
        print(f" {i}    |   {i*area}")
#Frågar om omstart        
    restart = input("Vill du köra igen Y/N ? ").lower()
        
#Beroende på vad man svarar tas man tilbaka till en funktion eller så
#avslutas programmet
    if "y" == restart:
            time.sleep(1)
            Räknare_A()
        
    elif "n" == restart:
            sys.exit(1)
            
    else:
        print("Du valde inget av alternativen")
        sys.exit(1)


start() 

    
    
    
    
    