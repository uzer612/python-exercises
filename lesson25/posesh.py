#coding: utf-8
kolvoLists = int(input())
o = 0
listAll = []
while kolvoLists > o:
    kolvoUchenikov = int(input())
    v = 0
    ucheniki = set()
    while v < kolvoUchenikov:
        uchenik = input()
        ucheniki.add(uchenik)
        v += 1
    listAll.append(ucheniki)
    o += 1
# /dannie vvedeny

# найти общие фамилии из всех множеств в списке

for i in range(0, len(listAll)-1):
    if (i == 0):
    	resultat = listAll[i] & listAll[i + 1]
    else:
        resultat = resultat & listAll[i + 1]

x = list(resultat)
x.sort()
for el in x:
    print(el)
