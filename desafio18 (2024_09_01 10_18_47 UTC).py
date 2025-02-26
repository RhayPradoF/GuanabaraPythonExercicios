#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, tan, cos # quando só faz o import da biblioteca completa tem que se fazer
#referência ao math.modulo a ser usada para que o programa entenda qual e a função que você quer usar

angulo = float(input("Informe o comprimento do ângulo: "))

seno = sin(radians(angulo))
print(f'O ângulo de{angulo} tem o SENO de {seno:.2f}')

cosseno = cos(radians(angulo))
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")

tangente = tan(radians(angulo))
print(f"O angulo de {angulo} tem a TANGENTE de {tangente:.2f}")
