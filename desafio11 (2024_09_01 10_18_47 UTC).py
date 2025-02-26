#desafio11 >> Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input("Informe a largura: "))
altura = float(input("Informe a altura: "))

#litro_tinta = 2**2 # 1 litro de tinta, pinta uma área de 2m²
area = largura*altura
quantidade_tinta = area / 2
print(f"sua parede tem a dimensão de {largura} x {altura} = área de {area}m².")
print(f"Para pintar uma sala inteira será {quantidade_tinta:.2f} litros de tinta ")

