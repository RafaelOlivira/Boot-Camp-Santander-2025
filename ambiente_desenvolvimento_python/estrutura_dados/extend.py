linguagens = ["Python","Java","VB.net","VBA"]

novas_linguagens = ["SQL","Golang","PHP","Javascript"]


linguagens.extend(novas_linguagens)

# print(linguagens)
# print(linguagens.index("Javascript"))

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
# print(numeros)

print(linguagens[-1]) # Ultimo elemento
