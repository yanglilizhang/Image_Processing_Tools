from skimage.filters import threshold_otsu, threshold_adaptive
import cv2

image = cv2.imread("shapes.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 将彩色图像转换为灰度图像
(t, thresh) = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)  # 对灰度图像进行二值化处理
cv2.imshow("Thresh",thresh)

#Contour
# 首先，它使用cv2.findContours函数查找图像中的轮廓，并将结果存储在cnts变量中。
# 然后，使用cv2.drawContours函数在原始图像上绘制轮廓，使用绿色线条以2的线宽
(_,cnts,_) = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for (i, c) in enumerate(cnts):
    cv2.drawContours(image,[c],-1,(0,255,0),2)

cv2.imshow("Contours",image)
cv2.waitKey(0)
