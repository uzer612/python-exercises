#coding: utf-8
from PIL import Image
im = Image.open("image.jpeg")
#print(im.size)
pixels = im.load()
x, y = im.size

sumR = 0
sumG = 0
sumB = 0
a = 0

for i in range(x):  
    for j in range(y):
        r, g, b = pixels[i, j]
        sumR += r
        sumG += g
        sumB += b
        a += 1

resR = sumR // a
resG = sumG // a
resB = sumB // a
print(resR, resG, resB)
#1. получить сумму всех r
#2. узнать кол-во чисел
#3. разделить на кол-во чисел сумму
