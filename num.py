spisok = [ "щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
num = int(input())
a = 0
b = 0
while a<num:
	if a >= len(spisok):
		print(spisok[b])
		b+=1
		a += 1
		if b == len(spisok):
			b = 0
	else:
		print(spisok[a])
		a += 1
