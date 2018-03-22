rows = int(input())
columns = int(input())

elements = []

c = 0
while c < rows * columns: 
	elements.append(input())
	c += 1


###########################################


a = 0
x = 0
while a < rows:
	b = 0
	res = ''
	while b < columns:
		res += elements[x] + '\t'
		x += 1
		b += 1
	print(res)
	a += 1
			



