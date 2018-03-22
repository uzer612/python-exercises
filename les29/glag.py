#coding: utf-8
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
wordList = ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть']
text = input()

t1 = text.replace(r'[\t\n\r\,\.]', '')
t = t1.split(' ')
#print(t)
a = 0
for el in t: 
	p = morph.parse(el)[0]
	if p.normal_form in wordList:
		a += 1
#		print(p, p.normal_form)

print(a)


#print(t1)