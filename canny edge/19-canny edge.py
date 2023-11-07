import  numpy as np
import cv2

image=cv2.imread("mycoins.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# 使用高斯模糊函数对图像进行平滑处理，ksize为核大小，(7,7)表示7x7的核大小
blur = cv2.GaussianBlur(gray, (7, 7), 0)
# 使用Canny边缘检测算法提取图像边缘信息，canny为边缘图像，blur为平滑后的图像，50和200为两个阈值
canny = cv2.Canny(blur, 50, 200)

cv2.imshow("Canny",canny)
cv2.waitKey(0)
