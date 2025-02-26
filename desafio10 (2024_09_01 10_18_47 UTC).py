#desafio10 >> Crie um programa que leia quanto dinherio a pessoa tem na carteira e mostre quantos dolares
#ela pode comprar. Considerando o dolar U$1.00 = R$3.27

carteira = float(input("Insira quanto você tem em sua carteira: R$ "))

dolar = carteira / 3.27

print(f"Com valor de R$ {carteira}, você terá o valor U${dolar:.2f}")