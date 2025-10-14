# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 08:52:52 2025

@author: heike
"""

#%%
"""
studieplan for


"""

#%%

def init_studieplan:
    return [[] for _ in range(6)]

def legg_til_i_studieplan (emner, studieplan):
    kode = input("Skriv in emne kode: ")
    emne = finn_emne (emne, kode)
    if not emne:
        print ("Emne finnes ikke")
        return