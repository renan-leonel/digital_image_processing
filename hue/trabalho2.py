import numpy as np
import cv2 as cv

def hue(h, m, x):
    startValue = np.mod((m - x)/2, 180)
    endValue = np.mod((m + x)/2, 180)

    start = h >= startValue
    end = h <= endValue
    
    h = h.astype(np.uint16)

    if endValue > startValue:
        h[start & end] = np.mod(h[start & end] + 90, 180).astype(np.uint8)
    else:
        h[start | end] = np.mod(h[start | end] + 90, 180).astype(np.uint8)

    h = h.astype(np.uint8)

    return h

def alteracao(img, m, x):
    cv.imshow('Original', img)
    cv.waitKey(0)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    cv.imshow('HSV', hsv)
    cv.waitKey(0)

    h,s,v = cv.split(hsv)
    h = hue(h,m,x)

    hsv = cv.merge([h,s,v])
    rgb = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

    cv.imshow('Alterada', rgb)
    cv.waitKey(0)

def main():
    a = cv.imread('image1.png')
    m = int(input("Matiz = "))
    x = int(input("X = "))

    alteracao(a,m,x)

if __name__ ==  '__main__':
    main()