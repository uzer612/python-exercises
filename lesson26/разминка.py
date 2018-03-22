colors = input()
string2 = ''
listRGB = colors.split(' ')
a = 0
while a < 3:
	string2 += str(255 - int(listRGB[a])) + ' '
	a += 1
print(string2.rstrip())