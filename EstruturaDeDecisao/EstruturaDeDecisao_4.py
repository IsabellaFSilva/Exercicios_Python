# -*- coding: utf-8 -*-
"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

"""
l = str(input("Digite uma letra: \n").lower())
if l == "a" or l== "e" or l== "i" or l=="o" or l== "u":
    print("A letra ",l ," é uma vogal!!!")
else:
    print("A letra ",l ," é uma consoante!!!")