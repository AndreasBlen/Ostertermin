#! usr/bin/env python3

# =======================================================================
# Ostertermin berechnen 
# (zu gegebenem Jahr / westlicher und orthodoxer Termin wird berechnet)
# =======================================================================

import datetime as dt
import sys
import locale

def osterDatum(jahr, ost_oder_west): 
    # ====================== # 
    # eigentliche Berechnung # 
    # ====================== # 
    ost = False
    if ost_oder_west == "ost": ost = True
    
    jh = jahr // 100
    mondschalt = (15 + (3 * jh + 3) // 4)  -  ((8 * jh + 13) // 25)  # print("Mondschaltung:", mondschalt) 
    sonnenschalt = 2 - (3 * jh + 3) // 4                            # print("Sonnenschaltung:", sonnenschalt) 
    if ost: mondschalt = 15; sonnenschalt = 0
    mondparm = jahr % 19                                            # print("Mondparameter:", mondparm)
    keim = (19 * mondparm + mondschalt) % 30                        # print("Keim für 1. Vollmond im Frühling:", keim)
    kalenderkorr = (keim + mondparm // 11) // 29                    # print("Kalenderkorrektur:", kalenderkorr)
    ostergrenze = 21 + keim - kalenderkorr                          # print("Ostergrenze:", ostergrenze)
    ersterSoImMaerz = 7 - (jahr + jahr // 4 + sonnenschalt)% 7      # print("Erster Sonntag im März:", ersterSoImMaerz)
    osterentfernung = 7 - (ostergrenze - ersterSoImMaerz) % 7       # print("Osterentfernung:", osterentfernung)
    osterdat = ostergrenze + osterentfernung                        # print("Osterdatum (\"März\"-Datum):", osterdat)
    
    if ost: osterdat = osterdat + (jahr // 100) - (jahr // 400) - 2 
    
    ostertag = osterdat
    ostermonat = "März" 
    if osterdat > 31: 
        ostermonat = "April"
        ostertag = osterdat - 31
        
    if osterdat > 61:       # nur möglich für orthodoxen Ostertermin
        ostermonat = "Mai"
        ostertag = osterdat - 61 
        
        

    ### print(ost_oder_west, ": ", jahr, " ist Ostern am ", ostertag, ". ", ostermonat, ".", sep="")
    return "%2d. " % ostertag + "%-5s" % ostermonat

    
# ---------------------------------------------
#   Start Hauptprogramm
#----------------------------------------------
# s = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
locale.setlocale(locale.LC_ALL, "german")
now = dt.datetime.now()
tagDat = now.strftime("%d.%m.%Y")
tagZeit = now.strftime("%H:%M")
woTag = now.strftime("%A")

print("Heute ist übrigens ", woTag, ", der ", tagDat, ", ", tagZeit, sep="") 

jahr = ""
# --------------------------------------------
# Jahr als Kommandozeilenparameter übergeben ? 
# --------------------------------------------

# argv: Liste der Kommandozeilenparameter
# argv[0]: Skriptname (unwesentlich) 
# argv[1]: erster Parameter 
### print("Anzahl Argumente:", len(sys.argv))
if len(sys.argv) > 1: 
    jahr = sys.argv[1]
else:
    jahr = input("Gib Jahr: ")
    
try:
    jahr = int(jahr)
except ValueError: 
    print("Die eingegebene Jahreszahl", jahr, "war ungültig!")
    exit()


print("\nOstertermine ab %4d:" % jahr)
print("=" * 21)
print(); 
print("+--------+--------------+--------------+") 
print("I  Jahr  I    westlich  I    orthodox  I") 
print("+--------+--------------+--------------+") 
for i in range(jahr, jahr + 10): 
    print("I  ", i, "  I   ", osterDatum(i, "west"), "  I   ", osterDatum(i, "ost"), "  I",sep="" )

print("+--------+--------------+--------------+") 
print()

