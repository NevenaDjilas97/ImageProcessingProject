#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math
from  PIL import Image
import os
import numpy as np
import math
import  matplotlib
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
#os.chdir("C:\\Users\\Nevena\\Desktop\\2020&2021 classes\\Introduction to image processing\\Image_Processing_Project")


from image import MyImage
from utils import hsv2rgb
from utils import rgb2hsv


def brightness(imageName, brightParameter):
    image = MyImage.open(imageName)
    #image = Image.open(imageName)
    for x in range(image.width - 1):
        for y in range(image.height - 1):
            rgb = image.getpixel((x, y))
            hsb = rgb2hsv(rgb[0], rgb[1], rgb[2])

            h, s, br = hsb
            s = s / 100
            br = br / 100
            br = br*brightParameter

            r, g, b = hsv2rgb(h, s, br)
            image.putpixel((x, y), (r, g, b))
    #im=image.arr()
    #impil=Image.fromarray(im)
    #impil.show()
    #image.show()
    image.save("brightness.jpg")
#brightness("sunrises.jpg",5)
def contrast(imageName, parameterCont):
    image = MyImage.open(imageName)

    for x in range(image.width):
        for y in range(image.height):
            rgb = image.getpixel((x, y))
            # skaliram piksele na range[0,1]
            red = rgb[0] / 255
            green = rgb[1] / 255
            blue = rgb[2] / 255
            # ovde je 0.5 trashold,ako je boja tamnija, kad se oduzme trashold ide u negativne, pa ce se mnozenjem
            # sa parametrom jos otici u tamnije, a ako je svetla, posvetlece se
            r = (((red - 0.5) * parameterCont) + 0.5) * 255
            g = (((green - 0.5) * parameterCont) + 0.5) * 255
            b = (((blue - 0.5) * parameterCont) + 0.5) * 255

            if r > 255:
                r = 255
            elif r < 0:
                r = 0
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            if b > 255:
                b = 255
            elif b < 0:
                b = 0
            image.putpixel((x, y), (r, g, b))
    image.save("contrast.jpg")

def blur(imageName, radius):
    image = MyImage.open(imageName)
    for x in range(image.width):
        for y in range(image.height):
            mat = [image.getpixel((x, y))]
            for i in range(1, radius):
                if x - i > 1 and x - i < image.width - 1:
                    if y + i > 1 and y + i < image.height - 1:
                        mat.append(image.getpixel((x - i, y + i)))
                    if y > 1 and y < image.height - 1:
                        mat.append(image.getpixel((x - i, y)))
                    if y - i > 1 and y - i < image.height - 1:
                        mat.append(image.getpixel((x - i, y - i)))
                if x > 1 and x < image.width - 1:
                    if y + i > 1 and y + i < image.height - 1:
                        mat.append(image.getpixel((x, y + i)))
                    if y > 1 and y < image.height - 1:
                        mat.append(image.getpixel((x, y)))
                    if y - i > 1 and y - i < image.height - 1:
                        mat.append(image.getpixel((x, y - i)))
                if x + i > 1 and x + i < image.width - 1:
                    if y + i > 1 and y + i < image.height - 1:
                        mat.append(image.getpixel((x + i, y + i)))
                    if y > 1 and y < image.height - 1:
                        mat.append(image.getpixel((x + i, y)))
                    if y - i > 1 and y - i < image.height - 1:
                        mat.append(image.getpixel((x + i, y - i)))

            sumR = 0
            sumG = 0
            sumB = 0
            for i in range(len(mat)):
                sumR = sumR + mat[i][0]
                sumG = sumG + mat[i][1]
                sumB = sumB + mat[i][2]
            r = sumR / len(mat)
            g = sumG / len(mat)
            b = sumB / len(mat)

            image.putpixel((x, y), (r, g, b))

    # return image.arr
    image.save("blur.jpg")

def sharpen(imageName, parameterSharp):
    image = MyImage.open(imageName)
    for x in range(image.width):
        for y in range(image.height):
            if x > 1 and x < image.width - 1 and y > 1 and y < image.height - 1:

                mat = [image.getpixel((x - 1, y + 1)), image.getpixel((x, y + 1)), image.getpixel((x + 1, y + 1)),
                       image.getpixel((x - 1, y)), image.getpixel((x, y)), image.getpixel((x + 1, y)),
                       image.getpixel((x - 1, y - 1)), image.getpixel((x, y - 1)), image.getpixel((x + 1, y - 1))]
                sumR = 0
                sumG = 0
                sumB = 0
                for i in range(8):
                    sumR = sumR + mat[i][0]
                    sumG = sumG + mat[i][1]
                    sumB = sumB + mat[i][2]
                BLUREDr = sumR / 9
                BLUREDg = sumG / 9
                BLUREDb = sumB / 9
                r = mat[4][0] + (mat[4][0] - BLUREDr) * parameterSharp
                g = mat[4][1] + (mat[4][1] - BLUREDg) * parameterSharp
                b = mat[4][2] + (mat[4][2] - BLUREDb) * parameterSharp
                if r > 255:
                    r = 255
                elif r < 0:
                    r = 0
                if g > 255:
                    g = 255
                elif g < 0:
                    g = 0
                if b > 255:
                    b = 255
                elif b < 0:
                    b = 0
                image.putpixel((x, y), (r, g, b))
    image.save("sharpen.jpg")

from tkinter.filedialog import askopenfilename

#current_value = Interface.comboboxFilter.get()
#def uploadImage():
   # root.filename = tk.filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  #filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

#def chooseFilter(currentvalue,)





