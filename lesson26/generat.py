#coding: utf-8
from random import choice
import string
listPassMem = []


def main(n, m):
	listPass = []
	Pass = ''
	a = 0
				
	while a < n:
		Pass = generate_password(m)
		listPass.append(Pass)
		a+=1
	return listPass


def generate_password(m):
	p = generate_unic_password(m)
	if p in listPassMem:
		return generate_password(m)
	listPassMem.append(p)
	return p


def generate_unic_password(m):
	strPass = ''
	x = 0
	while x < m:
		strPass += generate_sym()
		x+=1
	return strPass


def generate_sym():
	sym = choice(string.ascii_letters + string.digits)
	if sym in '0OIl1o':
		return generate_sym()
	return sym
