# -*- coding: utf-8 -*-
"""
Faça um Programa que leia três números e mostre o maior e o menor deles.

"""
n1 = input("Insira o 1º número --->")
n2 = input("Insira o 2º número --->")
n3 = input("Insira o 3º número --->")

maior = n1
menor = n1

if maior < n2:
	maior = n2

if maior < n3: 
	maior = n3

if menor > n2:
	menor = n2

if menor > n3:
	menor = n3
    
print("O maior número inserido foi ", maior)
print("O menor número inserido foi ", menor)

"""
if n1 > n2 and n1 > n3:
    print("O maior número inserido foi ",n1)
elif n2 > n1 and n2 > n3:
    print("O maior número inserido foi ",n2)
elif n3 > n1 and n3 > n2:
    print("O maior número inserido foi ",n3)
elif n1 == n2 or n1 == n3:
    print("O maior número inserido foi ",n1)
elif n2 == n1 or n2 == n3:
    print("O maior número inserido foi ",n2)
elif n3 == n1 or n3 == n2:
    print("O maior número inserido foi ",n1)
    
if n1 < n2 and n1 < n3:
    print("O menor número inserido foi ",n1)
elif n2 < n1 and n2 < n3:
    print("O menor número inserido foi ",n2)
elif n3 < n1 and n3 < n2:
    print("O menor número inserido foi ",n3)
elif n1 == n2 or n1 == n3:
    print("O menor número inserido foi ",n1)
elif n2 == n1 or n2 == n3:
    print("O menor número inserido foi ",n2)
elif n3 == n1 or n3 == n2:
    print("O menor número inserido foi ",n1)
"""

