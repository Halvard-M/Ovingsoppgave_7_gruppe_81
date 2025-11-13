# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:47:35 2025

@author: HM
emner
"""
class Emner():

    def __init__(self, navn ='N/A', kode ='N/A', semester = 'N/A', studiepoeng ='0'):
        self.navn = navn
        self.kode = kode
        self.semester = semester
        self.studiepoeng = studiepoeng
        pass

    def __str__(self):
        return f"Navn: {self.navn}, kode: {self.kode}, semester: {self.semester}, studiepoeng: {self.studiepoeng}"
        


def legg_til_emne(emner):
    Emne = Emner()
    Emne.navn = input("Emnenavn: ")
    Emne.kode = input("Emnekode: ")
    semester = input("Undervises i (høst/vår): ").lower()
    if semester not in ['høst', 'vår']:
        print("Ugyldig semester.")
        return
    else:
        Emne.semester = semester

    try:
        Emne.studiepoeng = int(input("Studiepoeng: "))
    except ValueError:
        print("Ugyldig antall studiepoeng.")
        return
    
    dicentry = {"Emne": Emne.navn, "kode": Emne.kode, "semester": Emne.semester, "studiepoeng": Emne.studiepoeng}
    emner.append(dicentry)
    print(f"Emnet {Emne.kode} er lagt til i lista (emner).")
    
def skriv_ut_emner(emner):
    if not emner:
        print("Ingen emner registrert.")
        return
    print("\nRegistrerte emner: ")
    for emne in emner:
        print(f"{emne['kode']} - Emne: {emne['Emne']} - {emne['semester']} - {emne['studiepoeng']} studiepoeng")
        
def finn_emne(emner, kode):
    for emne in emner:
        if emne['kode'] == kode:
            return emne
    return None

    
    