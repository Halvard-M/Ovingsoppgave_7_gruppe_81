# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:47:35 2025

@author: HM
emner
"""

def legg_til_emne(emner):
    kode = input("Emnekode: ")
    semester = input("Undervises i (høst/vår): ").lower()
    if semester not in ['høst', 'vår']:
        print("Ugyldig semester.")
        return
    try:
        studiepoeng = int(input("Studiepoeng: "))
    except ValueError:
        print("Ugyldig antall studiepoeng.")
        return
    
    emner.append({"kode" : kode, "semester" : semester,
                  "studiepoeng" : studiepoeng})
    print(f"Emnet {kode} er lagt til i lista (emner).")
    
def skriv_ut_emner(emner):
    if not emner:
        print("Ingen emner registrert.")
        return
    print("\nRegistrerte emner: ")
    for emne in emner:
        print(f"{emne['kode']} - {emne['semester']} - {emne['studiepoeng']} studiepoeng")
        
def finn_emne(emner, kode):
    for emne in emner:
        if emne['kode'] == kode:
            return emne
    return None

    
    