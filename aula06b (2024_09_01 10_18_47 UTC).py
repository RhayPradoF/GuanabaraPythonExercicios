#n = bool(input("Digite um valor:"))
#print(n)
#desafios3 Cie um programa que leia dois números e mostre a soma entre eles(exercicio1)

#desafio4 faça um programa que leia algo pelo teclado e mostre na tela seu tipo
#primitivo e todos as informações possiveis sobre ele

valor = input("Digite algo: ")
print("O tipo primitivo desse valor e : ", type(valor))
print("Tem espaços ?", valor.isspace())
print("E numerico?", valor.isnumeric())
print("Está maiúsculo ?", valor.isupper())
print("Está tudo minúsculo?", valor.islower())
