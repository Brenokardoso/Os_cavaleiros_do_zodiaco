palavra = str(input("Digite qualuqer palavra desejada:\n"))
texto = [palavra]
lista = list()
x = 0
def verifica_vogal(letra):
    for x in range(len(letra)):
        if(letra[x] in "aeiou"):
            pass
        else:
            lista.append(letra[x])
    return(letra)       
 






verifica_vogal(texto[0])
print(lista,end='\n')
