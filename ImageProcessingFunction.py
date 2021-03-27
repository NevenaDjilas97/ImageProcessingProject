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


kelvin_table = {
    1000: (255, 56, 0),
    1100: (255, 71, 0),
    1200: (255, 83, 0),
    1300: (255, 93, 0),
    1400: (255, 101, 0),
    1500: (255, 109, 0),
    1600: (255, 115, 0),
    1700: (255, 121, 0),
    1800: (255, 126, 0),
    1900: (255, 131, 0),
    2000: (255, 138, 18),
    2100: (255, 142, 33),
    2200: (255, 147, 44),
    2300: (255, 152, 54),
    2400: (255, 157, 63),
    2500: (255, 161, 72),
    2600: (255, 165, 79),
    2700: (255, 169, 87),
    2800: (255, 173, 94),
    2900: (255, 177, 101),
    3000: (255, 180, 107),
    3100: (255, 184, 114),
    3200: (255, 187, 120),
    3300: (255, 190, 126),
    3400: (255, 193, 132),
    3500: (255, 196, 137),
    3600: (255, 199, 143),
    3700: (255, 201, 148),
    3800: (255, 204, 153),
    3900: (255, 206, 159),
    4000: (255, 209, 163),
    4100: (255, 211, 168),
    4200: (255, 213, 173),
    4300: (255, 215, 177),
    4400: (255, 217, 182),
    4500: (255, 219, 186),
    4600: (255, 221, 190),
    4700: (255, 223, 194),
    4800: (255, 225, 198),
    4900: (255, 227, 202),
    5000: (255, 228, 206),
    5100: (255, 230, 210),
    5200: (255, 232, 213),
    5300: (255, 233, 217),
    5400: (255, 235, 220),
    5500: (255, 236, 224),
    5600: (255, 238, 227),
    5700: (255, 239, 230),
    5800: (255, 240, 233),
    5900: (255, 242, 236),
    6000: (255, 243, 239),
    6100: (255, 244, 242),
    6200: (255, 245, 245),
    6300: (255, 246, 247),
    6400: (255, 248, 251),
    6500: (255, 249, 253),
    6600: (254, 249, 255),
    6700: (252, 247, 255),
    6800: (249, 246, 255),
    6900: (247, 245, 255),
    7000: (245, 243, 255),
    7100: (243, 242, 255),
    7200: (240, 241, 255),
    7300: (239, 240, 255),
    7400: (237, 239, 255),
    7500: (235, 238, 255),
    7600: (233, 237, 255),
    7700: (231, 236, 255),
    7800: (230, 235, 255),
    7900: (228, 234, 255),
    8000: (227, 233, 255),
    8100: (225, 232, 255),
    8200: (224, 231, 255),
    8300: (222, 230, 255),
    8400: (221, 230, 255),
    8500: (220, 229, 255),
    8600: (218, 229, 255),
    8700: (217, 227, 255),
    8800: (216, 227, 255),
    8900: (215, 226, 255),
    9000: (214, 225, 255),
    9100: (212, 225, 255),
    9200: (211, 224, 255),
    9300: (210, 223, 255),
    9400: (209, 223, 255),
    9500: (208, 222, 255),
    9600: (207, 221, 255),
    9700: (207, 221, 255),
    9800: (206, 220, 255),
    9900: (205, 220, 255),
    10000: (207, 218, 255),
    10100: (207, 218, 255),
    10200: (206, 217, 255),
    10300: (205, 217, 255),
    10400: (204, 216, 255),
    10500: (204, 216, 255),
    10600: (203, 215, 255),
    10700: (202, 215, 255),
    10800: (202, 214, 255),
    10900: (201, 214, 255),
    11000: (200, 213, 255),
    11100: (200, 213, 255),
    11200: (199, 212, 255),
    11300: (198, 212, 255),
    11400: (198, 212, 255),
    11500: (197, 211, 255),
    11600: (197, 211, 255),
    11700: (197, 210, 255),
    11800: (196, 210, 255),
    11900: (195, 210, 255),
    12000: (195, 209, 255) }

kelvin_list = [ 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
               2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900,
               3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900,
               4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900,
               5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900,
               6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900,
               7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900,
               8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900,
               9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900,
               10000, 10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 
               10900,11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700, 
               11800, 11900, 12000]

qualityFactor=2



def fade_out(image_path, factor):   
    image=Image.open(image_path)
    w,h=image.size
    matrixR=[]#np.empty((w,h),dtype=np.int32)
    matrixG=[]#np.empty((w,h),dtype=np.int32)
    matrixB=[]#np.empty((w,h),dtype=np.int32)
    for i in range (0,h):
        rowlistR=[]
        rowlistG=[]
        rowlistB=[]
        for j in range (0,w):
            rowlistR.append(image.getpixel((j,i))[0]//factor)
            rowlistG.append(image.getpixel((j,i))[1]//factor)
            rowlistB.append(image.getpixel((j,i))[2]//factor)       
        matrixR.append(rowlistR)
        matrixG.append(rowlistG)
        matrixB.append(rowlistB)
    
    for k in range (10):     
        for i in range (0,h):
            for j in range (0,w):
                r=int(image.getpixel((j,i))[0]-matrixR[i][j])
                g=int(image.getpixel((j,i))[1]-matrixG[i][j])
                b=int(image.getpixel((j,i))[2]-matrixB[i][j])
                image.putpixel((j,i),(r,g,b))
                
        seq='fadeout'+str(k)
        image.save(seq,"JPEG",quality=80,optimize=True,progressive=False)
    
#fade_out('sunrises.jpg', 4)

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

    

def changeTemp(imagePath,image_save_path):
    image=Image.open(imagePath)
    file_type='.jpg'
            
   # for i in range(0, len(kelvin_list),qualityFactor):
    kelvin_value=kelvin_list[10]
    temp=kelvin_table[kelvin_value]
    r,g,b=temp
    color_matrix=(r / 255.0, 0.0, 0.0, 0.0, 0.0, g / 255.0, 0.0, 0.0, 0.0, 0.0, b / 255.0, 0.0)
    new_image=image.convert('RGB',color_matrix)
    kelvin_list_string=str(kelvin_list[10])
    seq=image_save_path+kelvin_list_string+file_type
    new_image.save(seq,"JPEG",quality=80,optimize=True, progressive=False)
    
#changeTemp('slika.jpeg','nova_slika')

def changeSaturation(imagePath, decimal):
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


def vignette_effect(imagePath):
    image=Image.open(imagePath)
    width,height=image.size
    

    for i in range(0, height):    
        for j in range (0,width):
   
      
            cord=(j,i)
            rgb=image.getpixel(cord)
        
            dx=2*j/width-1
            dy=2*i/height-1
            d=math.sqrt(dx*dx+dy*dy)
            if d>1.8:
                d=1.0
            r,g,b=rgb 
            hsv=rgb2hsv(r, g, b)    
            h,s,v=hsv
            s=s/100.00
            v=v/100.00*(1-d*0.80)
            rgb=hsv2rgb(h, s, v)
            r,g,b=rgb
            image.putpixel((j,i),(r,g,b))
            
    image.save("vignette.jpg",quality=80,optimize=True,progressive=False)
    print("gotovo vignette")
    
#vignette_effect('sunrises.jpg')    
    
            
def crop_image(image_path, from_x, from_y, to_x, to_y ):
    image=Image.open(image_path)
    difference_x=to_x-from_x
    difference_y=to_y-from_y
    new_image=Image.new(mode="RGB", size=(difference_x,difference_y))
    w,h=image.size
    l=0
    k=0
    for i in range (from_x, to_x):
        for j in range (from_y, to_y):
           
            new_image.putpixel((l,k), image.getpixel((i,j)))
            k+=1
        k=0
        l+=1
    print('gotov crop')
    new_image.save("cropped_image.jpeg",quality=80,optimize=True,progressive=False)
    return new_image
    
#crop_image('slika.jpeg', 0, 0, 500,500)


def zoom(image_path,pivot_x,pivot_y,factor):
    print('zoom')
    image=Image.open(image_path)
    w,h=image.size
    print(w,h,'to je w i h')
    x1=pivot_x-w//(2*factor)
    y1=pivot_y-h//(2*factor)
    
    x2=pivot_x+w//(2*factor)
    y2=pivot_y+h//(2*factor)
    
    difference_x=x2-x1
    difference_y=y2-y1
    
    print(x1,x2,y1,y2)
    image_croped=crop_image(image_path,x1,y1,x2,y2)
    
    
    zoomed_image=Image.new(mode="RGB", size=(w,h))
    
    sh=h/difference_y
    sw=w/difference_x

    for i in range (0,h):
        for j in range (0,w):
            #print(i,j)
            y=int(i/sh)
            x=int(j/sw)
            
            zoomed_image.putpixel((j,i), image_croped.getpixel((x,y)))
            
    zoomed_image.save("zoomed.jpg", quality=80,optimize=True, progressive=False)        
    
#zoom('sunrises.jpg', 500, 400, 2)    
    
    
def nearest_neighbour(new_width,new_height,image_path):
    image=Image.open(image_path)
    streched_image=Image.new(mode='RGB',size=(new_width,new_height))
    w,h=image.size
    
    sh=new_height/h
    sw=new_width/w
    
    for i in range(new_height):
        for j in range(new_width):
            y=int(i/sh)
            x=int(j/sw)
            
            streched_image.putpixel((j,i), image.getpixel((x,y)))
            
    streched_image.save('streched_image.jpeg',quality=80,optimize=True, progressive=False)
    
    
#nearest_neighbour(1920, 1080, 'slika.jpeg')
    





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
                
    pil_img=Image.fromarray((output).astype(np.uint8))  
                     # converting array to image
    

    width_relation=width/new_width
    height_relation=height/new_height
    
    
    dole_levo=round(height*sine)
    
    dole_desno=round(width*sine)
    
    pil_img.save("rotated_image.png")       
    
    nearest_neighbour(new_width+2*dole_desno+2,new_height+2*dole_levo+2,'rotated_image.png')
    
    image_streched=Image.open('streched_image.jpeg')
    w,h=image_streched.size
    center_x=w//2
    center_y=h//2
    
    crop_image('streched_image.jpeg', center_x-width//2, center_y-height//2, center_x+width//2, center_y+height//2)
    

#rotateImage('sunrises.jpg', 20)

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
    
#x`shadows('sunrises.jpg',-50)
    
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
           v=((v/100+1)**(2**(factor/200))-1)*100
           if v>100:
               v=100
           if v<0:
               v=0
           #v = 100-((1-v/100)**(2**(factor/100))*100)
           
           newrgb=hsv2rgb(hsv[0], hsv[1]/100,v/100)
           r,g,b=newrgb
           image.putpixel((j,i),(r,g,b))
                
    image.save("highlight.jpg")  
           
#highlights('sunrises.jpg', -50)

#rotateImage('slika.jpeg', 20)
    
#vignette_effect("slika.jpeg")

#rotateImage("slika.jpeg", 20)
#changeSaturation("slika.jpeg", 0.4)
#print(rgb2hsv(150, 200, 250))

#print(rgb2hsv(150, 200, 250))
#print(hsv2rgb(210, 0.4, 0.98))

    
        
    