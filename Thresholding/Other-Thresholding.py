import numpy as np
import cv2
 
# 加载图像为灰度图
image = cv2.imread('cameraman.tif',0)
cv2.imshow('Original', image)
 
# 将低于127的像素值设为0（黑色），高于127的像素值设为255（白色）
ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('1 Threshold Binary', thresh1)
 
# 将低于127的像素值设为255，高于127的像素值设为0（与上述代码相反）
ret,thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('2 Threshold Binary Inverse', thresh2)
 
# 将高于127的像素值截断（保持）在127（255参数未使用）
ret,thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('3 THRESH TRUNC', thresh3)
 
# 将低于127的像素值设为0，高于127的像素值保持不变
ret,thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('4 THRESH TOZERO', thresh4)
 
# 与上述代码相反，将低于127的像素值保持不变，高于127的像素值设为0
ret,thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('5 THRESH TOZERO INV', thresh5)
cv2.waitKey(0) 
    
cv2.destroyAllWindows()
