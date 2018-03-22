strNum = int(input())
a = 1
strList = []
while a <= strNum:
	stroka = input()
	a += 1
	strList.append(stroka)
charNum = int(input())
for string in strList:
	if len(string) >= charNum:
		print(string[charNum-1], end='')