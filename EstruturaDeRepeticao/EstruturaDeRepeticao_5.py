# -*- coding: utf-8 -*-
"""
Altere o programa anterior permitindo ao usuário informar as populações e as 
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

"""

a = float(input("Insira o país A: \n"))
b = float(input("Insira o país B: \n"))
taxA = float(input("Insira a taxa de crescimento do país A: \n"))
taxB = float(input("Insira a taxa de crescimento do país B: \n"))
anos = 0

while (a < b):
    anos += 1
    a = a +(a * taxA)
    b = b +(b * taxB)

print ("Foram necessários %i anos para o país A ultrapassar o país B\nPaís A: %i\nPaís B: %i" %(anos, a, b))
    

