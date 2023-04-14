import collections

nmr_jogador = []
nmr_votos = []
pct_votos = []


for x in range(1,3):
    print("Digite o seu numero de votação,obs,apenas numeros eate 23\n")
    numero = int(input("\n"))
    while((numero > 23) or (numero < 0)):
        numero = int(input("Numero inválido,digite novamente:\n"))
    nmr_jogador.append(numero)

contagem = collections.Counter(nmr_jogador)

for nmr_jogador,cont in contagem:
    print(f"{nmr_jogador} and {cont}")