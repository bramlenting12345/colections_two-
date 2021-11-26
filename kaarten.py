import random
# =======================================[-list-]==============================================================================
kaart = 1 

lijsje_nammen_kaarten = ["harten","klaveren","ruiter","shoppen"]
kaarten_plaatjes = ["boer","vrouw","aas","heer"]
kaarten_nummers = [1,2,3,4,5,6,7,8,9,10]
kaarten_totaal = []

# ========================================[-programma lisjt vullen-]==========================================================================
for i in lijsje_nammen_kaarten:                 

    for x in kaarten_nummers:                  
        kaarten = str(i) + " " + str(x)
        kaarten_totaal.append(kaarten)
    
    for q in (kaarten_plaatjes):
       kaarten_met_plaatjes = str(i) + " " + str(q)
       kaarten_totaal.append(kaarten_met_plaatjes)
for z in range(1,3):
    kaarten_totaal.append("joker")

#======================================[-programma 7 kaarten tonen-]================================================
for k in range(7):
    
    zeven_kaarten = random.choice(kaarten_totaal)
    kaarten_totaal.remove(zeven_kaarten)
    print("kaart " + (str(kaart)+(" : ") + (zeven_kaarten)))
    kaart = kaart + 1 

#=======================================[-programma print overige kaarten dek-]================================================    
print(kaarten_totaal)    