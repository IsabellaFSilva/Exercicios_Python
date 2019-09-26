# -*- coding: utf-8 -*-
"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""
print("Insira as notas bimestrais: \n")
n1 = int(input("Nota 1 ---> \n"))
n2 = int(input("Nota 2 ---> \n"))
n3 = int(input("Nota 3 ---> \n"))
n4 = int(input("Nota 4 ---> \n"))

total = n1 + n2 + n3 + n4
media = total / 4
print("A media de notas é: ", media)

