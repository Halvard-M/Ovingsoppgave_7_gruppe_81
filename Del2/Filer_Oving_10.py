# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:17:15 2025

@author: halvard
Filer og handtering
"""

import json

def lagre_til_fil(emner, studieplaner):
    data = {"emner": 
        [{"kode": emne.kode, "navn": emne.navn, "semester": emne.semester, "studiepoeng": emne.studiepoeng}
        for emne in emner],"studieplaner": []}
        
    for sp in studieplaner:
        plan_data = {"plan_id": sp.plan_id, "tittel": sp.tittel, "semestre": [[emne.kode for emne in sem]
                                                                              for sem in sp.semestre]}
        data["studieplaner"].append(plan_data)
        
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Data er lagret til fil.")
    
def les_fra_fil():
    from Emner_Oving_10 import Emne
    from Studieplan_Oving_10 import Studieplan
    
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Fant ingen fil å lese fra.")
        return [], []
        
    emner = [Emne(e["kode"], e["navn"], e["semester"], e["studiepoeng"])
             for e in data.get("emner", [])]
    
    studieplaner = []
    for sp_data in data.get("studieplaner", []):
        sp = Studieplan(sp_data["plan_id"], sp_data["tittel"])
        for i, sem in enumerate(sp_data["semestre"]):
            for kode in sem:
                emne = next((e for e in emner if e.kode == kode), None)
                if emne:
                    sp.semestre[i].append(emne)
        studieplaner.append(sp)
        
    print("Data er lest fra fil.")
    return emner, studieplaner