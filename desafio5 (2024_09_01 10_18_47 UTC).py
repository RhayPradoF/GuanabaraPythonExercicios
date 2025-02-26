#desafio5 >> Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input("Digite um número: "))

antecessor = num - 1
sucessor = num + 1

#print("O antecessor de {} e {}, o sucessor e {}".format(num, antecessor, sucessor))
#print(f"O antecessor e {antecessor:.0f} e o sucessor e {sucessor:.0f}")
#print(f"Analisando o {num:.0f}, seu antecessor será {num-1:.0f} e seu sucessor será {num+1:.0f}") prof João
print("Analisando {}, seu sucessor será {} e seu antecessor será {}".format(num, (num-1), (num+1))) #Guanabara
