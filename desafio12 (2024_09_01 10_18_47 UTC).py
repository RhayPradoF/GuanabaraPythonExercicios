#desafio12 >> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto

produto = float(input("Informe o valor do produto: R$ "))

desconto = 0.05

novo_preco = produto-(produto*desconto)

print(f"O novo valor do produto será,{novo_preco:.2f}")