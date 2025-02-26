#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

km = float(input("Quantos Kms foram percorridos ?"))
dias = float(input("Por quantos dias ele ficou alugado ? "))

vr_diaria = 60
vr_km = 0.15
total_aluguel = (km*vr_km)+(vr_diaria*dias)

print(f"O total a pagar pelo aluguel desse veículo será de: R$ {total_aluguel}")