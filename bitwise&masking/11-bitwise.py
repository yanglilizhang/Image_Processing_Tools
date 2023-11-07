import numpy as np
import cv2

# 创建两个300x300的全零图像
image1 = np.zeros((300,300), dtype="uint8")
image2 = np.zeros((300,300), dtype="uint8")

# 在image1上绘制一个矩形
cv2.rectangle(image1, (130,130), (170,170), (255), -1)

# 在image2上绘制一个圆形
cv2.circle(image2, (150,150), 100, 255, -1)

# 显示逻辑与操作结果
cv2.imshow("And", cv2.bitwise_and(image1, image2))

# 显示逻辑或操作结果
cv2.imshow("Or", cv2.bitwise_or(image1, image2))

# 显示逻辑异或操作结果
cv2.imshow("XOr", cv2.bitwise_xor(image1, image2))

# 显示逻辑非操作结果（对image1进行取反）
cv2.imshow("Not 1", cv2.bitwise_not(image1))

# 显示逻辑非操作结果（对image2进行取反）
cv2.imshow("Not 2", cv2.bitwise_not(image2))

# 等待用户按下任意键
cv2.waitKey(0)
