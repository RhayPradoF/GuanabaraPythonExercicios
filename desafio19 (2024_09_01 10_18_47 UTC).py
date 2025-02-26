# Um professor quer sortear um dos seus quatro alunos para apagar o quadro (ramdom). Faça
# um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import choice

primeiro_aluno = input("Insirá o nome do 1º aluno: ")
segundo_aluno = input("Insirá o nome do 2º aluno: ")
terceiro_aluno = input("Insirá o nome do 3º aluno: ")
quarto_aluno = input("Insirá o nome do 4º aluno: ")
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
escolhido = choice(lista)

print(f"O aluno escolhido foi {escolhido}")