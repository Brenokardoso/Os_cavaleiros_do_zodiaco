impar = []
par = []
todos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

for x in range(len(todos)):
    if (x == 0):
        print("zero is neutre\n")
    elif (x % 2 == 0):
        par.append(x)
    else:
        impar.append(x)

print(f"lista total{todos}\nlista par{par}\nlista {impar}")