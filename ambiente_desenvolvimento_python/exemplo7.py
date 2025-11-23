# Transformando um tupla com várias tuplas dentro em um dicionario!

tupla = (("Nome","Rafael"),("Idade","18"),("Genêro","Masculino"))

tupla_for_dic = dict((x,y) for x,y in tupla) # Transformando em dicionario

print(tupla_for_dic)