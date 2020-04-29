# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:53:47 2020

@author: oscar
"""

mensaje = input("mensaje a cifrar:").lower()
numero = int(input("numero de desplazamiento:"))
abecedario = "abcdefghijklmnñopqrstuvwxyz"
cifrado =""

for i in mensaje:
    if i in abecedario:
        posicion = abecedario.index(i)
        nueva = (posicion + numero) % len(abecedario)
        cifrado+=abecedario[nueva]
        
    print("texto cifrado:", cifrado,)
    
        
    