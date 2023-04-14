def fib(numero):
    resultado = list()
    a , b = 0 , 1
    while(numero != 0):
        resultado.append(a)
        a , b = b , a+b
        numero -= 1
    return(print(resultado))

numero = int(input("\n"))
fib(numero,end=' ')