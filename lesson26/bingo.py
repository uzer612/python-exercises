import random
listA = ''
a = 0
b = 0
c = 0



listb = []
def getUnicRandom():
    x = True
    while x:
        r = random.randint(1, 75)
        if r not in listb:
            listb.append(r)
            x = False
    return r

while c < 5:
    while a < 5:
        if a == 2 and c == 2:          
            listA += ' ' + str(0) 
        else:
            r = getUnicRandom()
            if  r < 10:
                listA += ' ' + str(r)
            else:
                listA += str(r) 
        if a < 4:
            listA += ' '
        a += 1
        b += 1
    print(listA)
    listA = ''
    c += 1
    a = 0

