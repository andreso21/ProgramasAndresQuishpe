# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:08:32 2021

@author: Usuario
"""

while True:
    x=input ("Ingrese el nummero que contaré: ")
    if x== 'q' or x == 'quit':
        break
    x=int (x)
    y=1
    while True:
        print (y)
        y=y+1
        if y>x:
            break