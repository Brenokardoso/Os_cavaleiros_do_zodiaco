vetor1 = [1,2,3,4,5,6,7,8,9,10]
vetor2 = [-1,92,83,74,65,56,47,38,29,19]
vetor3 = []
vetor4 = [10,55,99,77,88,66,35,44,69,25]


#for x in range(len(vetor1)):
#    vetor3 = vetor1 + vetor2 
#    print(x)
#    
#print(vetor3)

#vetor3 = vetor1+vetor2+vetor4
#print(sorted(vetor3))

for x in range(len(vetor1)):
    vetor3.append(vetor1[x])
    vetor3.append(vetor2[x])
    vetor3.append(vetor4[x])

print(vetor3)
