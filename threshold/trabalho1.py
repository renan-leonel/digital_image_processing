import numpy as np
import cv2 as cv

def limiarizacao(img, t, acima, brilho):
    if acima:
        x = img >= t
    else:
        x = img < t

    img = img.astype(int)

    if brilho > 0:
      img[x] = np.minimum(img[x] + brilho, 255)
    else:
      img[x] = np.maximum(img[x] + brilho, 0)

    img = img.astype(np.uint8)
    cv.imshow('image',img)
    cv.waitKey(0)

def main():
    img  = cv.imread('image2.png', 0)
    t = int(input("T = "))
    acima = bool(input("Acima (True | False) = "))
    brilho = int(input("Brilho = "))
    limiarizacao(img, t, acima, brilho)

if __name__ ==  '__main__':
    main()