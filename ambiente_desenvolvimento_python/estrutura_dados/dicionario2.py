dicionario = {
    'rafael':{'nome':'rafael','idade':18}
}

dicionario['rafael']['nome'] = "Oliveira"
print(dicionario['rafael'])

print(dicionario.get('rafael',{}))


print(dicionario.items())

print(dicionario.keys())