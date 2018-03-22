#coding:utf-8
from PIL import Image
im = Image.open("image.jpg")
pixels = im.load()
x, y = im.size

for i in range(x):  
    for j in range(y):
        R, G, B = pixels[i, j]

C = 0.2989 * R + 0.5870 * G + 0.1140 * B 

print(С)