numeros = [1,2,3,4,5]
numeros_maiores = [13,54,23,76]
resultado = list(map(lambda x:x*2,numeros_maiores))
print(f"esse é o resultado 1:{resultado}")



numeros2 = [1,2,3,4,5,6,7,8,9,10]
resultado2 = list(filter(lambda x:x % 3 == 0,numeros2)) #ela pega o primeiro "X" e ele fica posicionado pra ser o arg dps da vŕgula,logo apos voce coloca o seu valor de comparativo no segundo "X" e deixa a função trabalhar

print(f"esse é o resultado2{resultado2}")

pessoas = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Maria', 'idade': 30},
    {'nome': 'Pedro', 'idade': 20}
]
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa['idade'])

print(f"{pessoas_ordenadas}")
