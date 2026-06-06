# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:18:29 2019

@author: CV
"""

#display an image

import cv2
import numpy

img = cv2.imread('downloads/sakura.jpg')
print(str(type(img)))
cv2.imshow('Color', img)
cv2.waitKey()
cv2.destroyAllWindows()