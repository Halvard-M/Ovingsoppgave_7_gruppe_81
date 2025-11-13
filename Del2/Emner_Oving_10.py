# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 20:44:05 2025

@author: halvard
Øving 10
"""

class Emne: 
    def __init__(self, kode, navn, semester, studiepoeng):
        self.kode = kode.upper()
        self.navn = navn
        self.semester = semester.upper()
        self.studiepoeng = studiepoeng
    
    def __str__(self):
        sem_full = "Høst" if self.semester == 'H' else "Vår"
        return f"{self.kode} - {self.navn} - {sem_full} - {self.studiepoeng} studiepoeng"
    
    def er_høst(self):
        return self.semester == "H"
    def er_vår(self):
        return self.semester == "V"
    
def legg_til_emne(emner):
    while True: 
        kode = input("Emnekode: ").strip()
        if kode.upper() == "":
            print("Går tilbake til hovedmeny.")
            return
        if not kode:
            print("Du må skrive inn en kode.")
            continue
    
        while True:
            navn = input("Navn på emnet: ").strip()
            if navn.upper() == "":
                print("Tilbake til forje steg.")
                break
            
            while True:
                semester = input("Undervises i (H/V): ").upper()
                if semester == "":
                    break
                if semester not in ["H", "V"]:
                    print("Ugyldig semester. Bruk H for høst eller V for vår.")
                    continue
                
                while True: 
                    studiepoeng_input =input("Studiepoeng: ").strip()
                    if studiepoeng_input.upper() == "":
                        print("Tilbake til forje steg.")
                        break
                    try:
                        studiepoeng = int(studiepoeng_input)
                    except ValueError:
                        print("Ugyldig antall studiepoeng.")
                        continue

                    nytt_emne = Emne(kode, navn, semester, studiepoeng)
                    emner.append(nytt_emne)
                    print(f"Emnet {kode.upper()} ble lagt til.")
                    return
                
                if studiepoeng_input.upper() == "":
                    continue
            if semester.upper() == "":
                continue
        continue
                        
def skriv_ut_emner(emner):
    if not emner:
        print("Ingen emner registrert.")
        return
    print("\nRegistrerte emner: ")
    for emne in emner:
        print(emne)
        
def finn_emne(emner, kode):
    for emne in emner:
        if emne.kode.lower() == kode.lower():
            return emne
    return None


    
    
