# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 9:21:10 2025

@author: HM OMS
filer
"""

import numpy as np

def lagre_til_fil(emner, studieplan):

    max_len = max(len(emner),len(studieplan))

    if max_len != 0 and len(emner)<len(studieplan):
        emner = np.pad(emner, ((0,0),(0, max_len-len(emner))),'constant',constant_values='naa')

    output = np.hstack((emner,studieplan.reshape(-1,1)),dtype=object)

    np.savetxt('output.csv', output, delimiter=',', fmt='%s')

def les_fra_fil(emner, studieplan):
    input = np.genfromtxt('output.csv', dtype=str, delimiter=',')
    emner = input[:,[0,1,2]]
    studieplan = input[:,3]