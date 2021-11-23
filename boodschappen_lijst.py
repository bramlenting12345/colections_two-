# maak en programmatje die de gebruiker vraagt om boodschappen lijstje te maken.

# De gebruiker word gevraagd om een item aan het lijstje toe te voegen en na het toevoegen of er nog meer is toe te voegen.
# Een item uit de boodschappen lijst bestaat uit 2 delen (wat en hoeveel)
# Als een item 2x word opgegeven word deze maar 1 keer in het lijstje getoond met de totale hoeveelheid
# Als de gebruiker geen boodschappen meer wilt toevoegen word het totale lijstje aan de gebruiker getoond.


# ===================================[ variable ]==========================================
vraag_hoeveel = 0
vraag_wat = 0 

# ====================================[ lijst ]============================================
boodschappen_lijst = {}
# ====================================[ uitvoer ]==========================================



def bestellin_toevoegen(): 
    vraag_wat = input(" wat wilt u toevoegen : ? ")
    for x, y in boodschappen_lijst.items():
        if vraag_wat == x:
            vraag_hoeveel = int(input("hoeeveel " + (vraag_wat ) + " wilt u erbij hebben : ? " + "u heeft al " + str(y)+ " "))
            y = y + vraag_hoeveel
            boodschappen_lijst[x] =  y
            nog_meer_bestellen = input("wilt u nog meer bestellen j / n  ")
            
            if nog_meer_bestellen == "j":
                    bestellin_toevoegen()
            elif nog_meer_bestellen == "n":
                for x, y in boodschappen_lijst.items():
                        print(x,y)
                        exit()

            else:
                print("u kunt alleen maar antwoorden met j / n ")
                bestellin_toevoegen()
            

    
            
    vraag_hoeveel = int(input("hoeeveel " + (vraag_wat ) + " wilt u hebben : ? "))
    boodschappen_lijst[vraag_wat] = vraag_hoeveel
                                
    nog_meer_bestellen = input("wilt u nog meer bestellen j / n  ")
    if nog_meer_bestellen == "j":
             bestellin_toevoegen()
    elif nog_meer_bestellen == "n":
           for x, y in boodschappen_lijst.items():
                print(x,y)
                exit()
    else:
         print("u kunt alleen maar antwoorden met j / n ")
         bestellin_toevoegen()
                


def bestelling_opnemen():
    vraag_boodschappen=input("wilt u een boodchappen lijsje samen stellen  j / n : ")
    if vraag_boodschappen == "j":
        bestellin_toevoegen()
    elif vraag_boodschappen == "n":
         print("oke tot ziens ")
    else:
        print("u kunt allen maar antwoorden met j / n ") 
        bestelling_opnemen()



bestelling_opnemen()