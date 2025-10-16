# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 11:26:11 2025

@author: HM, HL, OMS, JMH
Oving 7 Gruppe 81
meny
"""
from emner import (legg_til_emne, skriv_ut_emner)
from studieplan import (legg_til_i_studieplan, skriv_ut_studieplan, sjekk_gyldighet, init_studieplan)
from filer import (lagre_til_fil, les_fra_fil)


emner = []
studieplan = init_studieplan()

def meny():
    print("\nMENY")
    print("1. Lag nytt emne")
    print("2. Legg til emne i studieplanen")
    print("3. Skriv ut ei liste over alle registrerte emner")
    print("4. Skriv ut studieplanen med hvilke emner som er i hvert semester")
    print("5. Sjekk om studieplanen er gyldig eller ikke")
    print("6. Lagre emnene og studieplan til fil")
    print("7. Les inn emnene og studieplan fra fil")
    print("8. Avslutt")
    
while True:
    meny()
    valg = input("Velg eit alternativ (1-8): ")
    if not valg.isdigit() or not (1 <= int(valg) <= 8):
        print("Ugyldig valg, prøv på nytt.")
        continue
    
    if valg == "1":
        legg_til_emne(emner)
    elif valg == "2":
        legg_til_i_studieplan(emner, studieplan)
    elif valg == "3":
        skriv_ut_emner(emner)
    elif valg == "4":
        skriv_ut_studieplan(studieplan, emner)
    elif valg == "5":
         sjekk_gyldighet(studieplan)
    elif valg == "6":
        lagre_til_fil(emner, studieplan)
    elif valg == "7":
        emner, studieplan = les_fra_fil(studieplan)
    elif valg == "8":
        print("Avslutter.")
        break
    else:
        print("Ugyldig valg.")

        


