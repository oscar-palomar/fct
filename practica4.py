# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:34:14 2020

@author: oscar
"""

print ("BIENVENIDO A EMPAREJADO.COM")
print ("NECESITAMOS CONOCER ALGUNOS DATOS SOBRE TI PARA ENCONTRAR TI PARA ENCONTRAR TU PAREJA IDEAL")

print ('menu:')
nombre = input('tu nombre:')
ano = int(input('año de nacimiento:'))
taburete = input('¿te gusta taburete? [si/no]')

edad = 2020-ano

print ('Hola,', nombre,'.Si no me equivoco, tienes', edad,'años' )

if (taburete=='si' or taburete=='Si' or taburete=='SI'):
    print("ok boomer. lo tuyo va ser un caso dificil")
else:
    print("bueno al menos es un comienzo. veremos que se puede hacer contigo.")
    
lista=[str(nombre),int(edad),str(taburete)]
for lista in range(1):
    print(lista)