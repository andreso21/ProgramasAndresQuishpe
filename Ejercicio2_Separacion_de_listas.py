# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:42:43 2021

@author: Usuario
"""

listaSw=[]
listaR=[]
listaDF=[]
lista=["R1","R2","R3",
       "S1","S2","S3",
       "R4","R5","PC",
       "Ps5"]
for i in lista:
    if 'S' in i:
        listaSw.append(i)
    elif "R" in i:
        listaR.append(i)
    else:
        listaDF.append(i)
            
print ('Switches: ',listaSw,'\nRouters: ',listaR,'\nDispositivos Finales: ',listaDF)

        
        
        