# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 08:52:52 2025

@author: heike
studieplan for gruppeoving 7
(legg_til_i_studieplan, skriv_ut_studieplan, sjekk_gyldighet, init_studieplan)

"""

from emner import finn_emne

class Studieplan():
    
    def __init__(self, ID, emnerliste):
        self.ID = ID
        self.emnerlsite = emnerliste
        pass 

    def __str__(self):
        return f"ID: {self.ID}, Emner: {self.emnerlsite}"


def init_studieplan():
    return [[] for _ in range(6)]

def legg_til_i_studieplan (emner, studieplan):
    kode = input("Skriv inn emne kode: ")
    emne = finn_emne (emner, kode)
    if not emne:
        print ("Emne finnes ikke")
        return
    try:
        semnr = int(input("Hvilket semester 1-6: "))
    except ValueError:
        print("Ugyldig tall")
        return
    if not 1 <= semnr <=6:
        print("Semester må være mellom 1-6")
        return
    sem_index = semnr - 1

    for semester in studieplan:
        if kode in semester:
            print("Emnet er allerede i studieplanen.")
            return
    if emne["semester"] == "høst" and semnr not in [1, 3, 5]:
        print("Dette er et høstemne og kan ikke legges inn i dette semesteret.")
        return
    if emne["semester"] == "vår" and semnr not in [2, 4, 6]:
        print("Dette er et våremne og kan ikke legges inn i dette semesteret.")
        return
    total_studiepoeng = sum(finn_emne(emner,k)["studiepoeng"] for k in studieplan[sem_index])
    if total_studiepoeng + emne ["studiepoeng"] >30:
        print("Emnet ble ikke lagt til. Det blir for mange studiepoeng i dette semesteret.")
        return
    studieplan[sem_index].append(kode)
    print(f"La til emnet {kode} i semester {semnr}.")

def skriv_ut_studieplan(studieplan, emner):
    print("\nStudieplan:")
    for i, semester in enumerate(studieplan):
        print(f"Semester {i+1}:")
        if not semester:
            print("Ingen emner.")
        else:
            for kode in semester:
                emne = finn_emne(emner, kode)
                print(f"Kode: {kode} - Emne: {emne['Emne']} - {emne['studiepoeng']} studiepoeng - {emne['semester']}")

def sjekk_gyldighet(studieplan, emner):
    print("\nGyldighetsjekk:")
    gyldig = True
    for i, semester in enumerate(studieplan):
        total = sum(finn_emne(emner, k)["studiepoeng"] for k in semester)
        if total != 30:
            print(f"Semester {i+1} har {total} studiepoeng (skal være 30)")
            gyldig = False
        if gyldig:
            print("Studieplanen er gylidg.")

def fjern_fra_studieplan(emner, studieplan):
    sem_index = int(input("Velg semester 1-6: ")) -1
    print(f"Semester {sem_index+1}: ")
    for kode in studieplan[sem_index]:
                emne = finn_emne(emner, kode)
                print(f"Kode: {kode} - Emne: {emne['Emne']} - {emne['studiepoeng']} studiepoeng - {emne['semester']}")

    kode = (input("Velg kode fra liste: "))
    studieplan[sem_index].remove(kode)
    return