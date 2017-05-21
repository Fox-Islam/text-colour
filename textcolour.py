# -*- coding: cp1252 -*-
import random
import numpy as np
import cv2
import os
import time

path = raw_input('File path? ') #Input the text file path
files = open(path + '.txt')
sentence = files.read()
words = sentence.split()

img = np.zeros((len(max(sentence.split(), key=len)),len(words),3), np.uint8)
imgs = []

def generate_image(shift,lastval):
    print("lastval: " + str(lastval))
    print("shift: " + str(shift))
    mini = 33 #65 if just letters
    maxi = 126 #122 if just letters
    lim = 255
    m = 0
    for j in words:
        n = 0
        for i in words[m]:
            val = ord(words[m][n])
            normval = lim*(val - mini)/(maxi - mini)
            img[n,m,0] = (normval + shift) % 255
            img[n,m,1] = (lastval) % 255
            img[n,m,2] = int((normval+lastval)/2) % 255
            n = n + 1
            lastval = normval
        m = m + 1


lastval = random.randint(-254,254)
shift = random.randint(-254,254)

generate_image(shift,lastval)
img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
img[img == 0] = np.median(img[img>0])
img = np.repeat(np.repeat(img,10, axis=0), 10, axis=1)

cv2.imwrite("colourwords " + str(shift) + ".png", img)

#cv2.imshow(str(shift),large)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
