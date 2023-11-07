import numpy as np
import cv2

import cv2

# 读取图像
image = cv2.imread("cameraman.tif")
# 获取图像的高度和宽度
(h, w) = image.shape[:2]
# 计算中心点坐标
x = w / 2
y = w / 2
# 计算旋转变换矩阵
m = cv2.getRotationMatrix2D((x, y), -90, 1)
# 应用旋转变换矩阵到图像上
cv2.warpAffine(image, m, (w, h), image)
cv2.imshow("Rotate",image)
cv2.waitKey(0)