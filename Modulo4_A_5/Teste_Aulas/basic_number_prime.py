n = int(input("Digite o seu tamanho de n"))
for x in range(2,10):
    for y in range(2,n):
        if ((x % y) == 0):
            print(f"{x} igual {x} * {y//x}")
            break
        else:
            print(f"{x} não é primo")