import numpy as np
import cv2
import cv2
import numpy as np

# 读取彩色图像
image = cv2.imread("color.jpg")
# 将彩色图像分离为B、G、R三个通道
(B, G, R) = cv2.split(image)
# 显示B通道图像
cv2.imshow("B", B)
# 显示G通道图像
cv2.imshow("G", G)
# 显示R通道图像
cv2.imshow("R", R)
# 将B、G、R三个通道合并为彩色图像并显示
cv2.imshow("Image", cv2.merge([B, G, R]))
# 创建与原图像相同大小全为黑色的图像，并显示为蓝、绿、红三个通道
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))

cv2.waitKey(0)
