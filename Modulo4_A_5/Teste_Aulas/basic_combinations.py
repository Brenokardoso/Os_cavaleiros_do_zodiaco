combination = list()
for x in [1,2,3,4,5,6,7,8,9,10]:
    for y in [5,1,7,8,9,3,6,4,2]:
        for z in ['a','b','c','d','e','f','g']:
            if (x != y) and (x != z) and (y!=z):
                combination.append((x,y,z))


print(combination)
