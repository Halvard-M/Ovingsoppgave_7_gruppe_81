# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 9:21:10 2025

@author: OMS
filer
"""

import numpy as np

def lagre_til_fil(emner, studieplan):

    kode_til_lagring = []
    semester_til_lagring = [] 
    studiepoeng_til_lagring = []
    studieplan_til_lagring = []

    for emne in emner:
        kode_til_lagring.append(emne['kode'])
        semester_til_lagring.append(emne['semester'])
        studiepoeng_til_lagring.append(emne['studiepoeng'])

    emner_til_lagring = np.column_stack((kode_til_lagring,semester_til_lagring,studiepoeng_til_lagring))
    emner_til_lagring = np.array(emner_til_lagring,dtype='<U16')

    studieplan_til_lagring = list(np.concatenate(studieplan))

    np.savetxt('emner.csv', emner_til_lagring, delimiter=',', fmt='%s')
    np.savetxt('studieplan.csv', studieplan_til_lagring, delimiter=',', fmt='%s')

def les_fra_fil(studieplan):
    emner = []
    emner_til_henting = np.genfromtxt('emner.csv', delimiter=',', dtype='<U16')
    studieplan_til_henting = np.genfromtxt('studieplan.csv', dtype=None, encoding=None)

    for emne in range(len(emner_til_henting)):
        kode = str(emner_til_henting[emne, 0])
        semester = str(emner_til_henting[emne, 1])
        poeng = int(emner_til_henting[emne, 2])
        emner.append({'kode' : kode, 'semester' : semester, 'studiepoeng' : poeng})

    for sem_index in range(len(studieplan_til_henting)):
        studieplan[sem_index].append(studieplan_til_henting[sem_index])

    return emner, studieplan
