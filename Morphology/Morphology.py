import cv2
import numpy as np

image = cv2.imread('morph.png', 0)

cv2.imshow('Original', image)
cv2.waitKey(0)

# Let's define our kernel size
# 这个函数使用numpy库创建一个5x5大小的矩阵，其中所有元素都被初始化为1，数据类型为无符号整数
kernel = np.ones((5,5), np.uint8)

# Now we erode
# 腐蚀操作函数 cv2.erode() 用于对输入图像进行腐蚀操作。腐蚀操作是通过将原始图像中的区域逐渐缩小，从而实现去除噪声和细节的效果
erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)

# 导入图像并进行膨胀操作
dilation = cv2.dilate(image, kernel, iterations = 1)

cv2.imshow('Dilation', dilation)
cv2.waitKey(0)

# Opening - Good for removing noise
# 形态学开操作是一种图像处理技术，用于去除图像中的小物体或噪声，通过使用指定的结构元素kernel来实现。
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey(0)

# Closing - Good for removing noise
# 闭操作是一种通过将图像中的孔洞填充来增强图像的形态学操作。函数的返回值是一个闭操作后的图像。
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(0)


cv2.destroyAllWindows()
