# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:34:29 2021

@author: Usuario
"""

acl=int(input("Ingrese el #6 de ACL: "))
if acl >= 1 and acl <= 99:
    print("Es una ACL estandar")
elif acl> 100 and acl < 199:
    print("Es una ACL extendida")
else:
    print("No es una # de ACL válido")