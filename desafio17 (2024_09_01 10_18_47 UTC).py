#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#retangulo, calcule e mostre o comprimeto da hipotenusa.

from math import hypot

co = float(input("Informe o comprimento do cateto oposto: "))
ca = float(input("Informe o comprimento do cateto adjacente: "))

print(f"O valor da hipotenusa e o {hypot(co,ca):.2f}")
