# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:16:01 2025

@author: halvard
Main/meny
"""

from Emner_Oving_10 import legg_til_emne, skriv_ut_emner, finn_emne
from Studieplan_Oving_10 import Studieplan
from Filer_Oving_10 import lagre_til_fil, les_fra_fil


emner = []
studieplaner = []

def meny():
    print("\nMENY")
    print("1. Lag nytt emne")
    print("2. Lag ny studieplan")
    print("3. Legg til eit emne i studieplanen")
    print("4. Skriv ut ei liste over alle registrerte emner")
    print("5. Skriv ut studieplanen med hvilke emner som er i hvert semester")
    print("6. Sjekk om studieplanen er gyldig")
    print("7. Lagre emnene og studieplan til fil")
    print("8. Les inn emnene og studieplan fra fil")
    print("9. Avslutt")
    print("\nØnsker du å gå tilbake eit hakk, trykk 'Enter'.")
    
while True:
    meny()
    valg = input("Velg eit alternativ (1-9): ").upper()
    
    if not valg.isdigit() or not (1 <= int(valg) <= 9):
        print("Ugyldig valg, prøv på nytt.")
        continue
    
    if valg == "1":
        legg_til_emne(emner)
        
    elif valg == "2":
        plan_id = input("Studieplan-ID: ")
        tittel = input("Tittel: ")
        sp = Studieplan(plan_id, tittel)
        studieplaner.append(sp)
        print(f"Studieplan '{tittel}' opprettet")
        
    elif valg == "3":
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
            
    elif valg == "4":
       skriv_ut_emner(emner)
       
    elif valg == "5":
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
             
    elif valg == "6":
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
            
    elif valg == "7":
        lagre_til_fil(emner, studieplaner)
        
    elif valg == "8":
        emner, studieplaner = les_fra_fil()
        
    elif valg == "9":
        print("Avslutter.")
        break
    else:
        print("Ugyldig valg.")