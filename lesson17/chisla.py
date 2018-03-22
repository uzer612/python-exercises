# coding: utf8
def fromStringToList(string, container): 
	a = string.split(' ')#возврашает ['22', "33"]
	for el in a:
		container.append(int(el))



c = '22 4678 99'
b = []		
fromStringToList(c, b)




