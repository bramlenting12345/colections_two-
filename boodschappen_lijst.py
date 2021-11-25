# maak en programmatje die de gebruiker vraagt om boodschappen lijstje te maken.

# De gebruiker word gevraagd om een item aan het lijstje toe te voegen en na het toevoegen of er nog meer is toe te voegen.
# Een item uit de boodschappen lijst bestaat uit 2 delen (wat en hoeveel)
# Als een item 2x word opgegeven word deze maar 1 keer in het lijstje getoond met de totale hoeveelheid
# Als de gebruiker geen boodschappen meer wilt toevoegen word het totale lijstje aan de gebruiker getoond.


vraag_hoeveel = 0 
vraag_wat = 0

boodchappen_lijsje = {}
#=====================================[-def bestelling-]===============================================

def bestelling_j_n():                                                                # begin van het programma 
    vraag_bestelling = input("wilt u een boodschappen lijsje samen stellen j / n ")  
    if vraag_bestelling=="j":
        check_dubbelen()
      





#=====================================[-def vervolg bestelling-]=======================================

def check_dubbelen():
    vraag_wat = input("wat wilt u toeveogen aan uw lijsje : ? ")

    for x,y in boodchappen_lijsje.items():
        if vraag_wat == x:
            vraag_hoeveel = str(input("hoeveel " + (vraag_wat) + "wilt u meer bestellen : ? " + "u heeft al " + (y)))
            y = y + vraag_hoeveel
            boodchappen_lijsje[x] = y 
            meer_bestellen = input("wilt u nog meer bestellen j / n ")

            if meer_bestellen == "j":
                check_dubbelen()
            elif meer_bestellen=="n":
                print(x,y)
                exit()
            else:
                print("u kunt alleen kiezen tussen j / n  ") 





            
        
    vraag_hoeveel = int(input("hoeveel " + (vraag_wat) + "wilt u bestellen ")) 
    boodchappen_lijsje[vraag_wat]=[vraag_hoeveel]
    meer_bestellen = input ("wilt u nog meer bestellen : ? ")
    if meer_bestellen == "j":
        check_dubbelen()
    elif meer_bestellen=="n":
        print(x,y)
        exit     
    else:
        print("u kunt aleen kiezen tussen j / n ")
     


bestelling_j_n()