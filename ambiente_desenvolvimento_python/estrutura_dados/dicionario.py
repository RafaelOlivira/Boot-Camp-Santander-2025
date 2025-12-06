# dicionario = {"Chave":[1,2,3],"Chave2":[4,5,6]}

# print(dicionario["Chave"][1])
# print(dicionario["Chave2"][1])


pessoa = {'nome':'Rafael','idade':18,'telefone':'1234-4555'}

# print(pessoa)

pessoa['telefone'] = '1111-1111'
pessoa['genero'] = 'Masculino'
# print(pessoa)

for chave,valor in pessoa.items():
    print(f"{chave.title()} - {valor}")