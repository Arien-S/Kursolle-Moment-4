#Moment 04

import sys

import time


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
        
    
    
    

def Räknare_A():


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
            
        
    if sida_1 == sida_2:
        print("Detta är en kvadrat")
            
    elif sida_1 != sida_2:
        print("Detta är en rektangel")
        
           
    try:
        höjd = int(input("Ange figurens höjd"))
            
    except ValueError:
        print("Du får endast skriva heltal")
        höjd = int(input("Ange figurens höjd"))
        
    if höjd < 0:
        höjd = 1
        
    elif höjd > 10:
        höjd = 10
        
    
    area = sida_1*sida_2

    time.sleep(1)
    print(f"Med dina angivna mått blir arean på din geometriska form {area}")
    time.sleep(1)
    print("Här är vad volymen blir beroende på olika höjder")
    time.sleep(1)
    print("Höjd  |  Volym\n--------------")

    for i in range(1,höjd+1):
        time.sleep(1)
        print(f" {i}    |   {i*area}")
        
    restart = input("Vill du köra igen Y/N ? ").lower()
        

    if "y" == restart:
            time.sleep(1)
            Räknare_A()
        
    elif "n" == restart:
            sys.exit(1)
            
    else:
        print("Du valde inget av alternativen")
        sys.exit(1)


start() 

    
    
    
    
    