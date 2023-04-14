a , b = 0 , 1
limite = int(input("Digite aé qual iteração de fribonacci você deseja:\n"))
while (limite != 0):
    print(f"{a}",end=",")
    a , b = b , a+b
    limite -= 1
