numero = int(input("Digite até que camada voce deseja:\n"))

for i in range(1, numero+1):  
    for j in range(1, i+1):  
        print(i, end='')  
    print()  