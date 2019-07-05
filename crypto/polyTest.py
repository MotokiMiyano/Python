# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:54:43 2018

@author: 18T0015
"""
from sympy import *

x = Symbol("x")
f = 1
Sa = [12467549603,123467598760,187970,2498778601,287688990,35,2,68888888888888888888888888888]
for i in range(len(Sa)):
    f = f*(x-Sa[i])
fa = expand(f)

poly = poly(fa)

print(poly.all_coeffs())



