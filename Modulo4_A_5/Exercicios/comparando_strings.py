string1 = "vamos comprar banana"
string2 = "vamos comprar banana"

def tamanho_compara(str1,str2):

    if len(str1) > len(str2):
        print(f"A string '{str1}' tem {len(str1)} de tamanho")
        string_maior = len(str1)
    elif len(str1) < len(str2):
        print(f"A string '{str2}' tem {len(str2)} de tamanho")
        string_maior = len(str2)
    else :
        print(f"As strings tem o mesmo tamanho")
        string_maior = len(str1) or len(str2)
        return((string_maior))
    return
    

def compara_igualdades(string1,string2):
    
    flag = 0
    if(tamanho_compara(string1,string2) == len(string1) and tamanho_compara(string1,string2) == len(string2)):
        for x in range(len(string1)):
            if(string1[x] == string2[x]):
                flag +=1
                if((flag) == len(string1)):
                    print(f"As strings são iguais\n")
    else:
        print(f"As strings são diferentes")






    
   

tamanho_compara(string1,string2)
compara_igualdades(string1,string2)



