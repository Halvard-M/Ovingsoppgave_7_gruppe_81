# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:16:01 2025

@author: HM, OMS, HL, JMH
Main/meny
"""

from Emner_Oving_10 import legg_til_emne, skriv_ut_emner, finn_emne, emner
from Studieplan_Oving_10 import Studieplan, fjern_fra_studieplan, finn_emne_i_studieplan, studieplaner
from Filer_Oving_10 import lagre_til_fil, les_fra_fil





def meny():
    print("\n1. Lag et nytt emne")
    print("2. Legg til et emne i en studieplan")
    print("3. Fjern et emne fra en studieplan")
    print("4. Skriv ut ei liste over alle registrerte emner")
    print("5. Lag en ny tom studieplan")
    print("6. Skriv ut en studieplan med hvilke emner som er i hvert semester")
    print("7. Sjekk om en studieplan er gyldig eller ikke")
    print("8. Finn hvilke studieplaner som bruker et oppgitt emne")
    print("9. Lagre emnene og studieplanene til fil")
    print("10. Les inn emnene og studieplanene fra fil")
    print("11. Avslutt")
    print("\nØnsker du å gå tilbake eit hakk, trykk 'Enter'.")
    
while True:
    meny()
    valg = input("Velg eit alternativ (1-11): ").upper()
    
    if not valg.isdigit() or not (1 <= int(valg) <= 11):
        print("Ugyldig valg, prøv på nytt.")
        continue
    
    if valg == "1":
        legg_til_emne(emner)
        
    elif valg == "2":
        if not studieplaner:
            print("Ingen studieplaner er opprettet")
            continue
        for i, sp in enumerate(studieplaner):
            print(f"{i+1}. {sp.tittel}")
        try:
            valg_sp = int(input("Velg studieplan: ")) - 1
            studieplaner[valg_sp].legg_til_i_studieplan(emner)
        except (ValueError, IndexError):
            print("Ugyldig valg.")
            
    elif valg == "3":
        if not studieplaner:
            print("Ingen studieplaner er opprettet.")
            continue
        
        for i, sp in enumerate(studieplaner):
            print(f"{i+1}. {sp.tittel}")
            
        try:
            valg_sp = int(input("Velg studieplan: ")) - 1
            fjern_fra_studieplan(emner, studieplaner[valg_sp])
        except (ValueError, IndexError):
            print("Ugyldig valg.")
            
    elif valg == "4":
        skriv_ut_emner(emner)
       
    elif valg == "5":
        plan_id = input("Studieplan-ID: ")
        tittel = input("Tittel: ")
        sp = Studieplan(plan_id, tittel)
        studieplaner.append(sp)
        print(f"Studieplan '{tittel}' opprettet")
       
    elif valg == "6":
         if not studieplaner:
             print("Ingen studieplaner er opprettet.")
             continue
         for i, sp in enumerate(studieplaner):
             print(f"{i+1}. {sp.tittel}")
         try: 
             valg_sp = int(input("Velg studieplan: ")) - 1
             studieplaner[valg_sp].skriv_ut_studieplan()
         except (ValueError, IndexError):
             print("Ugyldig valg.")
             
    elif valg == "7":
        if not studieplaner:
            print("Ingen studieplaner er opprettet.")
            continue
        for i, sp in enumerate(studieplaner):
            print(f"{i+1}. {sp.tittel}")
        try:
            valg_sp = int(input("Velg studieplan: ")) - 1
            studieplaner[valg_sp].sjekk_gyldighet()
        except (ValueError, IndexError):
            print("Ugyldig valg.")
            
    elif valg =="8":
        finn_emne_i_studieplan(emner, studieplaner)
            
    elif valg == "9":
        lagre_til_fil(emner, studieplaner)
        
    elif valg == "10":
        emner, studieplaner = les_fra_fil()
        
    elif valg == "11":
        print("Avslutter.")
        break
    else:
        print("Ugyldig valg.")