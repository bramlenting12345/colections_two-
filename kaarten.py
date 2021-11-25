import random

# =====================================[-opdracht-]===========================================================================

# Maak een programmatje die een standaard deck met kaarten genereerd (54 kaarten), deze schut en de bovenste 7 er afhaald op het scherm toont en daarna de overige kaarten in het deck.

# De volgende regels gelden voor dit programma:
# Het deck bestaat uit 4 “kleuren” (harten, klaveren, schoppen & ruiten)
# Iedere kleur heeft 13 kaarten (2 t/m 10, een boer, een vrouw, een heer en een aas)
# Er zitten ook 2 jokers in het deck
# ls je geen User Defined Functions gebruikt bestaat je code uit minder dan 18 regels (exclusief lege regels)
# Als je wel User Defined Functions gebruikt bestaat je code uit minder dan 28 regels (exclusief lege regels)

# ======================================[-eisen-]=============================================================================


# kaarten aantal = 54 stuks.
# 4 kleuren kaarten =  ruite , harten , klaver , schoppen 
kaart = 1

# =======================================[-list-]==============================================================================
lijsje_nammen_kaarten = ["harten","klaveren","ruiter","shoppen"]
kaarten_plaatjes = ["boer","vrouw","aas","heer"]
kaarten_nummers = [1,2,3,4,5,6,7,8,9,10]
kaarten_totaal = []

# ========================================[-programma-]==========================================================================


for i in lijsje_nammen_kaarten:                 # for loop namen kaarten 

    for x in kaarten_nummers:                   # for loop kaarten nummers 
        kaarten = str(i) + " " + str(x)
        kaarten_totaal.append(kaarten)
    
    for q in (kaarten_plaatjes):
       kaarten_met_plaatjes = str(i) + " " + str(q)
       kaarten_totaal.append(kaarten_met_plaatjes)
for z in range(1,3):
    kaarten_totaal.append("joker")

for k in range(7):
    
    zeven_kaarten = random.choice(kaarten_totaal)
    kaarten_totaal.remove(zeven_kaarten)
    print("kaart " + (str(kaart)+(" : ") + (zeven_kaarten)))
    kaart = kaart + 1
print(kaarten_totaal)    





















