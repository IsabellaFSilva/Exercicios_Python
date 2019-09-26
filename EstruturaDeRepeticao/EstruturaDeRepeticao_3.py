# -*- coding: utf-8 -*-
"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

"""

nome = input("Insira um nome com mais de 3 caracteres: \n")
while len(nome) <=3:
    nome = input("Insira um nome com mais de 3 caracteres: \n")

idade = int(input("Insira a idade entre 0 e 150 anos: \n"))
while idade < 0 or idade > 150:
    idade = int(input("Insira a idade entre 0 e 150 anos: \n"))
    
salario = float(input("Insira um salário mair que zero: \n"))
while salario < 0:
     salario = float(input("Insira um salário mair que zero: \n"))

sexo = input("Insira um sexo: (f) ou (m) \n".upper())
while sexo != "f" and sexo != "m" :
    sexo = input("Insira um sexo: (f) ou (m) \n")
    
estCivil = input("Insira o estado civil: \n(s), (c), (v), (d)".upper())
while estCivil != "s" and estCivil != "c" and estCivil != "v" and estCivil != "d":
    estCivil = input("Insira o estado civil: \n(s), (c), (v), (d)\n")