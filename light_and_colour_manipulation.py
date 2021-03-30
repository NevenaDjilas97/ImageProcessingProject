from utils import rgb2hsv
from utils import hsv2rgb
from  PIL import Image
import math
from image import MyImage
import numpy as np


def brightness(imageName, brightParameter):
    image = MyImage.open(imageName)
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


def saturation(imagePath, decimal):
    if decimal < 0.0:
        print("error")
        return 0

    image = MyImage.open(imagePath)
    for x in range(image.width - 1):
        for y in range(image.height - 1):
            cord = (x, y)
            rgb = image.getpixel(cord)
            hsb = rgb2hsv(rgb[0], rgb[1], rgb[2])

            h, s, b = hsb
            s = s / 100
            b = b / 100
            s = s * decimal
            if s > 1:
                s = 1
            r, g, b = hsv2rgb(h, s, b)
            image.putpixel((x, y), (r, g, b))

    image.save("saturation.jpg")
    print('gotovo')
    return 1

def shadows(image_path, factor):
    if factor < -100:
        factor = -100
    if factor > 100:
        factor = 100

    image = MyImage.open(image_path)
    width, height = image.getSize()

    for i in range(height):
        for j in range(width):
            rgb = image.getpixel((j, i))
            hsv = rgb2hsv(rgb[0], rgb[1], rgb[2])
            v = hsv[2]

            v = (v / 100) ** (2 ** (-factor / 100)) * 100

            newrgb = hsv2rgb(hsv[0], hsv[1] / 100, v / 100)
            r, g, b = newrgb
            image.putpixel((j, i), (r, g, b))
    print('gotovo')
    image.save("shadow.jpg")

def highlights(image_path, factor):
    if factor < -100:
        factor = -100
    if factor > 100:
        factor = 100

    image = MyImage.open(image_path)
    width, height = image.getSize()

    for i in range(height):
        for j in range(width):
            rgb = image.getpixel((j, i))
            hsv = rgb2hsv(rgb[0], rgb[1], rgb[2])
            v = hsv[2]
            v = ((v / 100 + 1) ** (2 ** (factor / 150)) - 1) * 100
            if v > 100:
                v = 100
            if v < 0:
                v = 0
            # v = 100-((1-v/100)**(2**(factor/100))*100)

            newrgb = hsv2rgb(hsv[0], hsv[1] / 100, v / 100)
            r, g, b = newrgb
            image.putpixel((j, i), (r, g, b))

    image.save("highlight.jpg")