#coding:utf-8
import numpy as np
inp = input()
iArr = inp.split(' ')
rows = int(iArr[0])
columns = int(iArr[1])
counter = 1

field = np.zeros((rows, columns), dtype='uint8')
for r in range(0, rows):
	for c in range(0, columns):
		field[r,c] = counter
		counter += 1


for r in range(0, rows):
	if r % 2 != 0:
		field[r] = field[r][::-1]
print(field)