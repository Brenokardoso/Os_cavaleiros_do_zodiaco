lista = [10,20,30,40,50]



def somas(arg1):
    soma = 0
    for x in range(len(arg1)):
        soma += arg1[x]
    print(soma)
    # return(print(soma))

def mults(arg2):
    mult = 1
    for x in range(len(arg2)):
        mult *= arg2[x]
    print(mult)
    # return(print(mult))

def finals():
    return(somas(lista),mults(lista))
    
    
finals()