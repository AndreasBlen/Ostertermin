#! usr/bin/env python3

# =================================================
# bewegliche Feiertage berechnen zu gegebenem Jahr 
# ==================================================

from datetime import date, datetime, timedelta
import sys
import locale

def osterDatum(jahr, ost_oder_west="west"): 
    # ====================================================================== # 
    # Osterdatum berechnen Formel von Gauss/Lichtenberg                      # 
    # Erweiterung für östliches Ostern wird nicht benötigt,                  #   
    # daher "ost_oder_west" als Default-Parameter gesetzt (Default="west")   #
    # Rückgabewert als Tupel (tt, mm, jjjj)
    # ====================================================================== #
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
    ostermonat = 3 
    if osterdat > 31: 
        ostermonat = 4
        ostertag = osterdat - 31
        
    if osterdat > 61:       # nur möglich für orthodoxen Ostertermin
        ostermonat = 5
        ostertag = osterdat - 61 
        
        

    ### print(ost_oder_west, ": ", jahr, " ist Ostern am ", ostertag, ". ", ostermonat, ".", sep="")
    return (ostertag, ostermonat, jahr)  
    

# --------------------------------------------
# Beginn Hauptprogramm 
# --------------------------------------------
locale.setlocale(locale.LC_ALL, "german")
now = datetime.now()
tagDat = now.strftime("%d.%m.%Y")
tagZeit = now.strftime("%H:%M")
woTag = now.strftime("%A")

# print("Heute ist übrigens ", woTag, ", der ", tagDat, ", ", tagZeit, sep="") 

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
    
(tt, mm, jj) = osterDatum(jahr)
print("Bewegliche Feiertage ", jahr, ":", sep="")
print(f"Im Jahr {jahr:4d} ist Ostern am {tt:02d}.{mm:02d}.") 

odate=datetime(day=tt, month=mm, year=jahr).date()
print()

td = timedelta(days=48)
d1 = odate-td
print(f"Rosenmontag:\t\t {d1.day:02d}.{d1.month:02d}.") 

td = timedelta(days=2)
d1 = odate-td
print(f"Karfreitag:\t\t {d1.day:02d}.{d1.month:02d}.") 
print(f"Ostersonntag:\t\t {tt:02d}.{mm:02d}.") 
td = timedelta(days=1)
d1 = odate + td
print(f"Ostermontag:\t\t {d1.day:02d}.{d1.month:02d}.") 

td = timedelta(days=39)
d1 = odate + td
print(f"Christi Himmelfahrt:\t {d1.day:02d}.{d1.month:02d}.") 

td = timedelta(days=49)
d1 = odate + td
print(f"Pfingstsonntag:\t\t {d1.day:02d}.{d1.month:02d}.") 

td = timedelta(days=50)
d1 = odate + td
print(f"Pfingstmontag:\t\t {d1.day:02d}.{d1.month:02d}.") 

td = timedelta(days=60)
d1 = odate + td
print(f"Fronleichnam:\t\t {d1.day:02d}.{d1.month:02d}.") 



