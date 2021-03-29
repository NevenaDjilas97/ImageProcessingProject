#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:25:12 2021

@author: aleksandar
"""
import numpy as np
from  PIL import Image
from utils import rgb2hsv
import matplotlib.pyplot as plt

class MyImage:
    
    
    def __init__(self, image_path):
        image=Image.open(image_path)
        self.image_path=image_path
        self.arr=np.array(image)
        self.width=self.arr[0].size//3
        self.height=self.arr.size//3//self.width
      
      

    def new(width,height):
        return MyImage(width, height)
    
    def getSize(self):
        return (self.width,self.height)
    
    def open(image_path):
        return  MyImage(image_path)
    
    
    
    
    def save(self,save_image_path):
       image=Image.fromarray(self.arr)
       image.save(save_image_path,quality=80,optimize=True, progressive=False)
    
    def getpixel(self,shape):
        w=shape[0]
        h=shape[1]
        r,g,b=self.arr[w][h]
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
        self.arr[w][h][0]=r
        self.arr[w][h][1]=g
        self.arr[w][h][2]=b
    

    def convert(self):
        print('soon')
        
    def histogramHSV(self):
        histogram=[]
        for i in range (self.height):
            for j in range(self.width):
                r,g,b=self.getpixel((j,i))
                hsv=rgb2hsv(r,g,b)
                histogram[int(hsv[0])]+=1
        return histogram           
     
    def histogramRGB(self):
        histogramrgb=np.zeros((256,3))
        for i in range (self.height):
            for j in range(self.width):
                r,g,b=self.getpixel((j,i))
                histogramrgb[r][0]+=1
                histogramrgb[g][1]+=1
                histogramrgb[b][2]+=1
        
        plt.hist(histogramrgb,density=True,bins=30)
        plt.xlabel('NUMBER')
        plt.ylabel('RGB')
        plt.title('HISTOGRAM')
        plt.show()
                
        
#image=MyImage.open('sunrises.jpg')
#image.histogramRGB()
    
rgb=(1,1,1)
print(rgb+2)           

#image=MyImage.open('test.jpg')i2mage.histogram()
'''w,h=image.getSize()
for i in range(0,h):
    for j in range (0,w):
        image.getpixel((j,i))
        '''

        