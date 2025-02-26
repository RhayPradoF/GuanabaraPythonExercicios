#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todos as inforações possíveis sobre ele.

msg = input("Escreva algo: ")
print(type(msg))
print(msg.isalnum())
print(msg.isalpha())
print(msg.islower())
print(msg.isupper())