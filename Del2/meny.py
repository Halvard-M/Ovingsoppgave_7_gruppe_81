# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 11:26:11 2025

@author: HM, HL, OMS, JMH
Oving 7 Gruppe 81
meny
"""
from emner import (legg_til_emne, skriv_ut_emner)
from studieplan import (legg_til_i_studieplan, skriv_ut_studieplan, sjekk_gyldighet, init_studieplan, fjern_fra_studieplan)
from filer import (lagre_til_fil, les_fra_fil)


emner = []
studieplan = init_studieplan()

def meny():
    print("\nMENY")
    print("1. Lag nytt emne")
    print("2. Legg til emne i studieplanen")
    print("3. Fjern emne fra studieplanen")
    print("4. Skriv ut ei liste over alle registrerte emner")
    print("5. Skriv ut studieplanen med hvilke emner som er i hvert semester")
    print("6. Sjekk om studieplanen er gyldig eller ikke")
    print("7. Lagre emnene og studieplan til fil")
    print("8. Les inn emnene og studieplan fra fil")
    print("9. Avslutt")
    
while True:
    meny()
    valg = input("Velg eit alternativ (1-9): ")
    if not valg.isdigit() or not (1 <= int(valg) <= 8):
        print("Ugyldig valg, prøv på nytt.")
        continue
    
    if valg == "1":
        legg_til_emne(emner)
    elif valg == "2":
        legg_til_i_studieplan(emner, studieplan)
    elif valg == "3":
        fjern_fra_studieplan(emner, studieplan)
    elif valg == "4":
        skriv_ut_emner(emner)
    elif valg == "5":
        skriv_ut_studieplan(studieplan, emner)
    elif valg == "6":
         sjekk_gyldighet(studieplan)
    elif valg == "7":
        lagre_til_fil(emner, studieplan)
    elif valg == "8":
        emner, studieplan = les_fra_fil(studieplan)
    elif valg == "9":
        print("Avslutter.")
        break
    else:
        print("Ugyldig valg.")

        


