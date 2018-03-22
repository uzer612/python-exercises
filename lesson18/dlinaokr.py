#coding: utf8
def circleLength(radius):
	pi = 3.14159
	a1 = 2*float(pi)*float(radius)
	return a1

def circleArea(radius):
	pi = 3.14159
	a = float(pi)*float(radius)*float(radius)
	return a

def main():
	r = float(input())
	x1 = circleLength(r)
	x2 = circleArea(r)
	print(x1, x2)