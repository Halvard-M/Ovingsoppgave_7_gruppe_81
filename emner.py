# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:47:35 2025

@author: HM
emner
"""
def legg_til_emne(emner):
    kode = input("Emnekode: ")
    semester_høst = input("Undervises i (1, 3, 5): ")
    if semester_høst not in ['1', '3', '5']:
        print("Ugyldig semester.")
        return
    semester_vår = input("Undervises i (2, 4, 6): ")
    if semester_vår not in ['2', '4', '6']:
        print("Ugyldig semester.")
        return
    try:
        studiepoeng = int(input("Studiepoeng: "))
    except ValueError:
        print("Ugyldig antall studiepoeng.")
        return
    
    emner.append({"kode" : kode, "semester_høst" : semester_høst, "semester_vår" : semester_vår,
                  "studiepoeng" : studiepoeng})
    print(f"Emnet {kode} lagt til.")
    
def skriv_ut_emner(emner):
    if not emner:
        print("Ingen emner registrert.")
        return
    print("\nRegistrerte emner: ")
    for emne in emner:
        print(f"{emne['kode']}: {emne['semester']}: {emne['studiepoeng']} studiepoeng")
        
def finn_emne(emner, kode):
    for emne in emner:
        if emne['kode'] == kode:
            return emne
    return None

    
    