#nome = input("Qual e o seu nome? ")
#print("Prazer em te conhecer {}!".format(nome))

#print(f"A soma vale {n1+n2:.0f}") também pode ser usado mais fácil prof João ensinou assim
#print("A soma vale {}".format(n1+n2)) #Guanabara ensinou assim

n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1// n2
e = n1 ** n2
#print("A soma é {}, o produto é {} e a divisão é {}".format(s, m, d))
#print("A soma é {}, o produto é {} e a divisão é {:.2}".format(s, m, d)) # para uso de casas decimais
#print("A soma é {}, o produto é {} e a divisão é {:.2f}".format(s, m, d)) # casas decimais flutuantes
#print("A soma é {}, o produto é {} e a divisão é {:.3f}".format(s, m, d), end=" ") # para não pular linha
print("A soma é {},\n o produto é {} \n e a divisão é {:.3f}".format(s, m, d), end=" ") # para pular uma linha
print("\n Divisão inteira será {} \n e potência será {}".format(di, e))


#desafio5 >> Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
#desafio6 >> Crie um algoritmo que leia um número e mostre o seu dobro, triplo, e raiz quadrada
#desafio7 >> Deselvolva um programa que leia as duas notas de um aluno, calcule e mostre a média
#desafio8 >> Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros
#desafio9 >> Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
#desafio10 >> Crie um programa que leia quanto dinherio a pessoa tem na carteira e mostre quantos dolares
#ela pode comprar. Considerando o dolar U$1.00 = R$3.27
#desafio11 >> Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
#desafio12 >> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto
#desafio13 >> Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


