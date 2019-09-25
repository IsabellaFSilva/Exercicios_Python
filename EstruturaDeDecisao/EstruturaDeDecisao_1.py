# -*- coding: utf-8 -*-
"""
Faça um Programa que peça dois números e ;imprima o maior deles.

"""
num1 = int(input("Insira o Primeiro número: \n"))
num2 = int(input("Insira o Segundo número: \n"))
if num1 > num2 :
    print("O maior número é : ", num1)
elif num2 > num1 :
    print("O maior número é : ", num2)
else:
    print("Número Igual!!!")