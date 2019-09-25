#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
user = str(input("Insira um nome de usuário: \n").upper())
senha = str(input("Insira uma senha: \n").upper())
while user == senha:
    senha = str(input("A senha não pode ser igual ao usuário, insira a senha novamente: \n"))
    
print("User: %s --- Senha: %s" %(user, senha))