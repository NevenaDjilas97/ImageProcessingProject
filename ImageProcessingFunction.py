#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 01:13:28 2021

@author: aleksandar
"""

from utils import rgb2hsv
from utils import hsv2rgb
from  PIL import Image
import math
from image import MyImage

import numpy as np


def fade(image_path, factor):   
    if factor<0:
        factor=0
    if factor>100:
        factor=100
    a = np.array(Image.open("sunrises.jpg"), dtype=np.float32)
  
    b=a*0.67+8+factor/2

    Image.fromarray(np.uint8(np.rint(b))).save("fade.jpg")    

#fade('sunrises.jpg',100)


def warmmth(image_path,factor):
    if factor<-50:
        factor=-50
    if factor>50:
        factor=50
        
    image=MyImage.open(image_path)
    w,h=image.getSize()
    for i in range(0,h):
        for j in range (0,w):
            rgb=image.getpixel((j,i))
            r,g,b=rgb[0],rgb[1],rgb[2]
            if factor > 0:
                r+=factor
                if r>255:
                    r=255
                
            else:
                b+=-factor
                if b>255:
                    b=255
            image.putpixel((j,i),(r,g,b))
                
    image.save('warmth.jpg')
    print('gotovo')
            
#warmmth('sunrises.jpg', 50)


def saturation(imagePath, decimal):
    if decimal<0.0:
        print ("error")
        return 0
    
    image=MyImage.open(imagePath)
    for x in range(image.width-1):
        for y in range(image.height-1):
            cord=(x,y)
            rgb=image.getpixel(cord)
            hsb=rgb2hsv(rgb[0], rgb[1], rgb[2])
            
            h,s,b=hsb
            s=s/100
            b=b/100
            s=s*decimal
            if s>1:
                s=1
            r,g,b=hsv2rgb(h,s,b)
            image.putpixel((x,y),(r,g,b))
           
    image.save("saturation.jpg")        
    print('gotovo')
    return 1

#changeSaturation('sunrises.jpg', 0.4)


def vignette_effect(imagePath,factor):
    image=MyImage.open(imagePath)
    width,height=image.getSize()
    print(width,height)

    for i in range(0, width):    
        for j in range (0,height):
   
            cord=(i,j)
            rgb=image.getpixel(cord)
             
        
            dx=2*i/width-1
            dy=2*j/height-1
            d=math.sqrt(dx*dx+dy*dy)
            if d>1.8:
                d=1.0
            r,g,b=rgb 
            hsv=rgb2hsv(r, g, b)    
            h,s,v=hsv
            s=s/100.00
            #factor should be between 0.5 and 1
            v=v/100.00*(1-d*factor)
            rgb=hsv2rgb(h, s, v)
            r,g,b=rgb
            
            
            image.putpixel((i,j),(r,g,b))
            
            
    image.save("vignette.jpg")
    print("gotovo vignette")
    
#vignette_effect('sunrises.jpg',0.95)    
    
            
def crop_image(image_path, from_x, from_y, to_x, to_y ):
    image=MyImage.open(image_path)
    difference_x=to_x-from_x
    difference_y=to_y-from_y

    print(from_x,to_x)
    print(from_y,to_y)
    new_image=MyImage.new(difference_x,difference_y)
    w,h=image.getSize()
    l=0
    k=0
    for i in range (from_x, to_x-1):
        for j in range (from_y, to_y-1):
            new_image.putpixel((l,k), image.getpixel((i,j)))
            k+=1
        k=0
        l+=1
    new_image.save("cropped_image.jpeg")
    return new_image

#crop_image('sunrises.jpg', 100, 0, 600, 600)     


def zoom(image_path,pivot_x,pivot_y,factor):
    
    image=MyImage.open(image_path)
    w,h=image.getSize() 
    
    x1=pivot_x-w//(2*factor)
    y1=pivot_y-h//(2*factor)
    
    x2=pivot_x+w//(2*factor)
    y2=pivot_y+h//(2*factor)
    
    difference_x=x2-x1
    difference_y=y2-y1
    
    
    image_croped=crop_image(image_path,x1,y1,x2,y2)
    
    print('nesto2')
    

    
    zoomed_image=MyImage.new(w,h)
    
    sh=h/difference_y
    sw=w/difference_x

    for i in range (0,h):
        for j in range (0,w):
            #print(i,j)
            y=int(i/sh)
            x=int(j/sw)
            
            zoomed_image.putpixel((j,i), image_croped.getpixel((x,y)))
            
    zoomed_image.save("zoomed.jpg")           

#zoom('sunrises.jpg', 400, 300, 2)    
    
    
def nearest_neighbour(new_width,new_height,image_path):
    image=MyImage.open(image_path)
    streched_image=MyImage.new(new_width,new_height)
    w,h=image.getSize()
    
    sh=new_height/h
    sw=new_width/w
    
    for i in range(new_height):
        for j in range(new_width):
            y=int(i/sh)
            x=int(j/sw)
            
            streched_image.putpixel((j,i), image.getpixel((x,y)))
            
    streched_image.save('streched_image.jpeg')
    
#nearest_neighbour(1920, 1080, 'sunrises.jpg')
    




def rotateImage(imagePath,angle):
    image = np.array(Image.open(imagePath)) 
    angle=math.radians(angle) 
    cosine=math.cos(angle)
    sine=math.sin(angle)
    height=image.shape[0]  
    width=image.shape[1]    
    
    new_height  = round(abs(image.shape[0]*cosine)+abs(image.shape[1]*sine))+1
    new_width  = round(abs(image.shape[1]*cosine)+abs(image.shape[0]*sine))+1

    print(new_height,new_width)

    output=np.zeros((new_height,new_width,image.shape[2]))
    output=output.astype(np.uint8)

    # Find the centre of the image about which we have to rotate the image
    original_centre_height   = round(((image.shape[0]+1)/2)-1)    #with respect to the original image
    original_centre_width    = round(((image.shape[1]+1)/2)-1)    #with respect to the original image


    # Find the centre of the new image that will be obtained
    new_centre_height= round(((new_height+1)/2)-1)        #with respect to the new image
    new_centre_width= round(((new_width+1)/2)-1)          #with respect to the new image
    
 
    for i in range(height):
        for j in range(width):
            #co-ordinates of pixel with respect to the centre of original image
            y=image.shape[0]-1-i-original_centre_height                   
            x=image.shape[1]-1-j-original_centre_width                      
            
            #co-ordinate of pixel with respect to the rotated image
            new_y=round(-x*sine+y*cosine)
            new_x=round(x*cosine+y*sine)

            '''since image will be rotated the centre will change too, 
            so to adust to that we will need to change new_x and new_y with respect to the new centre'''
            new_y=new_centre_height-new_y
            new_x=new_centre_width-new_x

        # adding if check to prevent any errors in the processing
            if 0 <= new_x < new_width and 0 <= new_y < new_height and new_x>=0 and new_y>=0:
                output[new_y,new_x,:]=image[i,j,:]                          #writing the pixels to the new destination in the output image
                
        
    new_image=MyImage.new(new_width, new_height)
    new_image.arr=output
        
    #pil_img=Image.fromarray((output).astype(np.uint8))  
                     # converting array to image
    
    width_relation=width/new_width
    height_relation=height/new_height
    
    
    dole_levo=round(height*sine)
    
    dole_desno=round(width*sine)
    
    new_image.save("rotated_image.png")       
    
    nearest_neighbour(new_width+2*dole_desno+2,new_height+2*dole_levo+2,'rotated_image.png')
    
    image_streched=MyImage.open('streched_image.jpeg')
    w,h=image_streched.getSize()
    center_x=w//2
    center_y=h//2
    
    crop_image('streched_image.jpeg', center_x-width//2, center_y-height//2, center_x+width//2, center_y+height//2)
    

rotateImage('sunrises.jpg', 20)

def shadows(image_path, factor):
    if factor<-100:
        factor=-100
    if factor>100:
        factor=100
        
    image=MyImage.open(image_path)
    width,height=image.getSize()
    
    for i in range(height):
        for j in range(width):
           
           rgb=image.getpixel((j,i))
           hsv=rgb2hsv(rgb[0], rgb[1], rgb[2])
           v=hsv[2]
                
           v = (v/100)**(2**(-factor/100))*100
           
           newrgb=hsv2rgb(hsv[0], hsv[1]/100, v/100)
           r,g,b=newrgb
           image.putpixel((j,i),(r,g,b))
    print('gotovo')
    image.save("shadow.jpg") 
    
#shadows('sunrises.jpg',-50)
    
def highlights(image_path,factor):
    if factor<-100:
        factor=-100
    if factor>100:
        factor=100
        
    image=MyImage.open(image_path)
    width,height=image.getSize()
    
    for i in range(height):
        for j in range(width):
           rgb=image.getpixel((j,i))
           hsv=rgb2hsv(rgb[0], rgb[1], rgb[2])
           v=hsv[2]
           v=((v/100+1)**(2**(factor/150))-1)*100
           if v>100:
               v=100
           if v<0:
               v=0
           #v = 100-((1-v/100)**(2**(factor/100))*100)
           
           newrgb=hsv2rgb(hsv[0], hsv[1]/100,v/100)
           r,g,b=newrgb
           image.putpixel((j,i),(r,g,b))
                
    image.save("highlight.jpg")  
   
#highlights('sunrises.jpg', 50)     
    
def test():
    imagepillow=Image.open('sunrises.jpg')
    imagemoja=MyImage.open('sunrises.jpg')
    
    print(imagepillow.size)
    print(imagemoja.getSize())
    
   #print('pill',pillw,pillh)
   # print('moja',mojaw,mojah)
   # for i in range(w):
       # for j in range (h):
            
            
#test()
    
#highlights('sunrises.jpg', -50)

#rotateImage('slika.jpeg', 20)
    
#vignette_effect("slika.jpeg")

#rotateImage("slika.jpeg", 20)
#changeSaturation("slika.jpeg", 0.4)
#print(rgb2hsv(150, 200, 250))

#print(rgb2hsv(150, 200, 250))
#print(hsv2rgb(210, 0.4, 0.98))

    
        
    