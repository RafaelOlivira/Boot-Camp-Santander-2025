import numpy as np

qtd_notas = int(input("Digite a quantidade de notas a ser inseridas: "))

notas = []
for i in range(qtd_notas):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota)
media = np.mean(notas) # Usando a biblioteca numpy para calcular a média com a função mean()

print(f"Média das notas: {media}")