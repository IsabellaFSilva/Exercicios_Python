#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a 
#letra escrever: F - Feminino, M - Masculino, Sexo Inválido
sexo = str(input("Insira o Sexo: (F) ou (M)\n").upper())
if sexo == "M":
    print("Masculino")
elif sexo == "F":
    print("Feminino")
else:
    ("Sexo Inválido")