import os

tupla_nomes = set()
while True:
    nome = input("Digite um nome para a lista: ").lower().strip()
    if nome == "":
        os.system("cls")
        print("Fim")
        print("Tupla de Nomes")
        for index,nome in enumerate(tupla_nomes):
            print(f"{index+1}º {nome}")
        break    
    tupla_nomes.add(nome)
