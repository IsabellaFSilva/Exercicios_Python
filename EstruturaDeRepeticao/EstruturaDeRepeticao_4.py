# -*- coding: utf-8 -*-
"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma 
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
número de anos necessários para que a população do país A ultrapasse ou iguale 
a população do país B, mantidas as taxas de crescimento.

"""

a = 80000
b = 200000
taxA = 0.03
taxB = 0.015
anos = 0

while (a < b):
    anos += 1
    a = a +(a * taxA)
    b = b +(b * taxB)

print ("Foram necessários %i anos para o país A ultrapassar o país B\nPaís A: %i\nPaís B: %i" %(anos, a, b))
    

