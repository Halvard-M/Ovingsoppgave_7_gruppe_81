# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 9:21:10 2025

@author: HM OMS
filer
"""

import numpy as np

def lagre_til_fil(filer):
    np.savetxt('fil.csv', , delimiter=';', header='', comments='')

def les_fra_fil(filer):
    data = np.genfromtxt('fil.csv', delimiter=';', missing_values='N/A', skip_header=1)
    print(data)