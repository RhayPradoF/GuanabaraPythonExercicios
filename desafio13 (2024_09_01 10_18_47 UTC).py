#desafio13 >> Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe o seu salário atual: R$ "))

aumento = 1.15

novo_salario = salario*aumento

print(f"Seu novo salário será de R$ , {novo_salario:.2f}")