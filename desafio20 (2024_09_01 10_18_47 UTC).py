# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

from random import shuffle

primeiro_aluno = input("Insirá o nome do 1º aluno: ")
segundo_aluno = input("Insirá o nome do 2º aluno: ")
terceiro_aluno = input("Insirá o nome do 3º aluno: ")
quarto_aluno = input("Insirá o nome do 4º aluno: ")
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
shuffle(lista)

print("A ordem dos alunos a apresentar será: ")
print(lista)