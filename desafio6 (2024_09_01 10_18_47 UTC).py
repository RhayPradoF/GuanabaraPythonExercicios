#desafio6 >> Crie um algoritmo que leia um número e mostre o seu dobro, triplo, e raiz quadrada

num = int(input("Digite um número: "))

dobro = num *2
triplo = num *3
raiz = num ** (1/2) # pode usar também o pow

print("O dobro e :", dobro)
print("O triplo e: ", triplo)
print(f"A raiz quadrada desse número e: ", raiz{:.2f})
