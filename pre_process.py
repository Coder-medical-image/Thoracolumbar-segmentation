import cv2
import numpy as np

# 加载图像并进行预处理
img = cv2.imread('D:/Graduationproject/transunet_pytorch-main/img/1.png', 0)  # 以灰度模式加载图像
img1 = cv2.GaussianBlur(img, (5, 5), 0)  # 添加高斯滤波



# img_hist_eq_old = cv2.equalizeHist(img)  # 对图像进行直方图均衡
img_hist_eq = cv2.equalizeHist(img1)  # 对图像进行直方图均衡


# 可选：显示原始图像和均衡化后的图像
cv2.imshow('Original Image', img)
cv2.imshow('GaussianBlur',img1)
cv2.imshow('Histogram Equalized Image', img_hist_eq)
# cv2.imshow('Histogram Equalized Image_old', img_hist_eq_old)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # cv2.imwrite('Original Image.png', img)
# cv2.imwrite('GaussianBlure.png', img1)


