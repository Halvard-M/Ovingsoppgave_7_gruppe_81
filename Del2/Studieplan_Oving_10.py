# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 21:04:42 2025

@author: HM, OMS, HL, JMH
Studieplan
"""
studieplaner = []

from Emner_Oving_10 import Emne, finn_emne

class Studieplan:
    def __init__(self, plan_id, tittel):
        self.plan_id = plan_id
        self.tittel = tittel
        self.semestre = [[] for _ in range (6)]
        
    def legg_til_i_studieplan(self, emner):
        kode = input("Skriv inn emnekode: ").upper()
        emne = finn_emne(emner, kode)
        if not emne: 
            print("Emnet finnes ikkje.")
            return
        
        try:
            semnr = int(input("Hvilket semester (1-6): "))
        except ValueError:
            print("Ugyldig tall.")
            return
        
        if not 1 <= semnr <= 6:
            print("Semester må vere mellom 1 og 6.")
            return
        sem_index = semnr - 1
        
        #For å unngå duplikater
        for semester in self.semestre:
            if any(e.kode == kode for e in semester):
                print("Emnet er allerede i studieplanen.")
                return
            
        #Sjekk semester gyldighet
        if emne.semester == "H" and semnr not in [1, 3, 5]:
            print("Dette er et høstemne og kan ikkje legges til her.")
            return
        if emne.semester == "V" and semnr not in [2, 4, 6]:
            print("Dette er et våremne og kan ikkje legges til her.")
            return
            
        #Studiepoeng sjekk
        total_stp = sum(e.studiepoeng for e in self.semestre[sem_index])
        if total_stp + emne.studiepoeng > 30:
            print("For mange studiepoeng i dette semesteret.")
            return
        
        self.semestre[sem_index].append(emne)
        print(f"La til {emne.kode} i semester {semnr}.")
    
    def skriv_ut_studieplan(self):
        print(f"\nStudieplan: {self.tittel} (ID: {self.plan_id})")
        for i, semester_emner in enumerate(self.semestre, start=1):
            if semester_emner:
                print(f"Semester {i}:")
                for emne in semester_emner:
                    print(f"   {emne}")                   
            else:
                print(f"Semester {i}: (Ingen emner registrert.")
                
    def sjekk_gyldighet(self):
        print("\nGyldighetssjekk:")
        gyldig = True
        for i, semester in enumerate(self.semestre):
            total = sum(emne.studiepoeng for emne in semester)
            if total != 30:
                print(f"Semester {i+1} har {total} studiepoeng (Bør vere 30).")
                gyldig = False
        if gyldig:
            print("Studieplanen er gyldig.")
        else:
            print("Studieplanen er ugyldig.")
        
def finn_emne_i_studieplan(emner, studieplaner):
    emnekode = input("Skriv inn emnekoden til emnet du vil finne: ").upper()
    funnet = False
    
    for plan in studieplaner:
        for semnr, semester in enumerate(plan.semestre, start=1):
            for emne in semester:
                if emne.kode == emnekode:
                    print(f"Emnet {emnekode} finnes i studieplan {plan.tittel} (ID: {plan.plan_id}) i semester {semnr}.")
                    funnet = True
    if not funnet:
        print(f"Ingen studieplaner har {emnekode}.")
            
def fjern_fra_studieplan(emner, studieplan):
    try:
        sem_index = int(input("Velg semester 1-6: ")) -1
    except ValueError:
        print("Ugyldig tall.")
        return
        
    if not 0 <= sem_index <6:
        print("Ugyldig semester.")
        return
    
    semester = studieplan.semestre[sem_index]
    if not semester:
        print(f"Semester {sem_index+1} er tomt.")
        return
    
    print(f"\nSemester {sem_index+1}:")
    for i, emne in enumerate(semester):
        print(f"{i+1}. {emne.kode} - {emne.navn} ({emne.studiepoeng} stp)")
    try:
        valg = int(input("Velg emnet du vil fjerne: ")).upper() -1
        fjernet_emne = semester.pop(valg)
        print(f"Fjernet {fjernet_emne.kode} fra semester {sem_index+1}.")
    except (ValueError, IndexError):
        print("Ugyldig valg, tallet til emne du vil fjerne.")
        
        

    
        
                    
        


