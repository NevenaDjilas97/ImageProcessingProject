    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:25:12 2021

@author: aleksandar
"""
import numpy as np
from  PIL import Image
import matplotlib.pyplot as plt



class MyImage:
    
    
    def __init__(self, image_path='prazno',width=0,height=4):
        if width==0:
            image=Image.open(image_path)
            self.image_path=image_path
            self.arr=np.array(image)
            self.width=self.arr[0].size//3
            self.height=self.arr.size//3//self.width
        else:
            self.width=width
            self.height=height
            self.arr=np.empty((height,width,3),dtype=np.int8)
            self.arr=self.arr.astype(np.uint8)
            
      

    def new(width,height):
        return MyImage('bezveze',width, height)
    
    def getSize(self):
        return (self.width,self.height)
    
    def open(image_path):
        return  MyImage(image_path,0,0)
    
    
    
    
    def save(self,save_image_path):
       image=Image.fromarray(self.arr)
       image.save(save_image_path,quality=80,optimize=True, progressive=False)
    
    def getpixel(self,shape):
        w=shape[0]
        h=shape[1]
        r,g,b=self.arr[h][w]
        return (r,g,b)
        
    def putpixel(self,shape, rgb):
        w,h=shape[0],shape[1]
        r,g,b=rgb[0],rgb[1],rgb[2]
        if r<0:
            r=0
        if r>255:
            r=255
        if g <0:
            g=0
        if g>255:
            g=255
        if b<0:
            b=0
        if b>255:
            b=255
        self.arr[h][w][0]=r
        self.arr[h][w][1]=g
        self.arr[h][w][2]=b

def histogram(slika):
    image = MyImage.open(slika)
    w, h = image.getSize()
    red = []
    green = []
    blue = []
    for x in range(w):
        for y in range(h):
            rgb = image.getpixel((x, y))
            red.append(rgb[0])
            green.append(rgb[1])
            blue.append(rgb[2])
    plt.hist(red, 256, density=1, facecolor='r', alpha=0.5)
    plt.hist(green, 256, density=1, facecolor='g', alpha=0.5)
    plt.hist(blue, 256, density=1, facecolor='b', alpha=0.5)
    plt.xlabel('value')

    plt.show()

arr=np.zeros((2,5))
print(arr)
        
#image=MyImage.open('sunrises.jpg')
#image.histogramRGB()
    
#rgb=(1,1,1)
#print(rgb+2)           

#image=MyImage.open('test.jpg')i2mage.histogram()
'''w,h=image.getSize()
for i in range(0,h):
    for j in range (0,w):
        image.getpixel((j,i))
        '''

        