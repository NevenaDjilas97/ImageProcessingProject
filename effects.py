
import math
from  PIL import Image
import numpy as np
import math
from image import MyImage
from utils import hsv2rgb
from utils import rgb2hsv

def fade(image_path, factor):
    if factor < 0:
        factor = 0
    if factor > 100:
        factor = 100
    a = np.array(Image.open("sunrises.jpg"), dtype=np.float32)

    b = a * 0.67 + 8 + factor / 2

    Image.fromarray(np.uint8(np.rint(b))).save("fade.jpg")

    # fade('sunrises.jpg',100)

def vignette_effect(imagePath, factor):
    image = MyImage.open(imagePath)
    width, height = image.getSize()
    print(width, height)

    for i in range(0, width):
        for j in range(0, height):

            cord = (i, j)
            rgb = image.getpixel(cord)

            dx = 2 * i / width - 1
            dy = 2 * j / height - 1
            d = math.sqrt(dx * dx + dy * dy)
            if d > 1.8:
                d = 1.0
            r, g, b = rgb
            hsv = rgb2hsv(r, g, b)
            h, s, v = hsv
            s = s / 100.00
            # factor should be between 0.5 and 1
            v = v / 100.00 * (1 - d * factor)
            rgb = hsv2rgb(h, s, v)
            r, g, b = rgb

            image.putpixel((i, j), (r, g, b))

    image.save("vignette.jpg")
    print("gotovo vignette")

# vignette_effect('sunrises.jpg',0.95)
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

