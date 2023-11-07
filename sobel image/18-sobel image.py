import numpy as np
import cv2

image=cv2.imread("mycoins.jpg")
# 这个函数将输入图像转换为灰度图，并对灰度图进行Sobel边缘检测操作，得到x和y方向的边缘图像
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gx = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)  # x方向上的Sobel边缘检测
gy = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)  # y方向上的Sobel边缘检测

gx = cv2.convertScaleAbs(gx)  # 将gx图像进行比例缩放并转换为绝对值
gy = cv2.convertScaleAbs(gy)  # 将gy图像进行比例缩放并转换为绝对值

cv2.imshow("Gx",gx)
cv2.imshow("Gy",gy)

# 对gx和gy分别进行Sobel运算，权重分别为0.5，然后相加，得到边缘增强图像
sobel = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)
cv2.imshow("Sobel Image",sobel)
cv2.waitKey(0)