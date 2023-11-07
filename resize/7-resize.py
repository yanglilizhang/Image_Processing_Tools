import cv2

image = cv2.imread("cameraman.tif")
(h,w) = image.shape[:2]
#height
r = 50/float(w)  # 计算宽高比
dim = (50,int(r*h))  # 根据宽高比计算新的图像尺寸
image0 = cv2.resize(image.copy(),dim,cv2.INTER_AREA)  # 调整图像大小到新的尺寸
cv2.imshow("Resize-H",image0)
#wight
r = 50/float(h)
dim = (int(r*h),50)
image1 = cv2.resize(image.copy(),dim,cv2.INTER_AREA)
cv2.imshow("Resize-W",image1)


cv2.waitKey(0)