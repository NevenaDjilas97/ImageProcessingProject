# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math



def rgb2hsv(r, g, b):
        
    r=r/255.0
    g=g/255.0
    b=b/255.0
    
    cmax=max(r,g,b)
    cmin=min(r,g,b)
    
    diff=cmax-cmin
    
    h=-1
    
    s=-1    
    
    if cmax==cmin:
        h=0
    elif cmax==r:
        h=(60*((g-b)/diff)+360)%360
    elif cmax==g:
        h = (60 * ((b - r) / diff) + 120) % 360 
    elif cmax==b:
        h = (60 * ((r - g) / diff) + 240) % 360
    
    if cmax==0:
        s=0
    else:
        s=(diff/cmax)*100
    v=cmax*100
    
    hsv=[h,s,v]

    return hsv
        
    

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0:
        r, g, b = v, t, p
    elif hi == 1: 
        r, g, b = q, v, p
    elif hi == 2: 
        r, g, b = p, v, t
    elif hi == 3:
        r, g, b = p, q, v
    elif hi == 4:
        r, g, b = t, p, v
    elif hi == 5:
        r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

print(rgb2hsv(150, 150, 150))

print(hsv2rgb(0, 0, 58.8))