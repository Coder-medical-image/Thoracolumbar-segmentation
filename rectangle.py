import cv2
import numpy as np
from matplotlib import pyplot as plt

# path = r"D:\Graduationproject\transunet_pytorch-main\mask\2.png"
path = r"D:\Graduationproject\transunet_pytorch-main\2_old.png"
# 加载图像
image = cv2.imread(path)
print(image)
# 使用Canny边缘检测来找到等高线
image = cv2.GaussianBlur(image,(3,3),0)
edges = cv2.Canny(image, 200, 200)
edges = cv2.Canny(image,800,200,apertureSize=5)
#
print(edges)

# 找到等高线的轮廓
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# 对于每个轮廓，计算并绘制其边界矩形
for contour in contours:
    rect = cv2.minAreaRect(contour)

    box = cv2.boxPoints(rect)
    box = np.int0(box)
    # cv2.drawContours(image, [box], 0, (0, 0, 255), 2)
    cv2.drawContours(image, [box], -1, (0, 255, 0), 2)


    # print(rect)
    # x, y, w= rect
    # print(type(x))
    # print(x)
    # cv2.rectangle(image, (x, y), (x + w, y ), (0, 255, 0), -1)  # 填充矩形框颜色
    # cv2.rectangle(image, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), -1)  # 填充矩形框颜色
    # cv2.rectangle(image, (rect[0][0], rect[0][1]), (rect[0][2], rect[0][3]), (0, 255, 0), -1)  # 填充矩形框颜色
#
#



# 显示图像
cv2.imshow('Image with bounding rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('saved_image.jpg', image)



# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# # path = r"D:\Graduationproject\transunet_pytorch-main\mask\2.png"
# path = r"D:\Graduationproject\transunet_pytorch-main\2.png"
# # 加载图像
# img = cv2.imread(path)
#
#
# edges = cv2.Canny(img,800,200,apertureSize=5)
# edges2 = cv2.Canny(img,2000,200)
# plt.subplot(131),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# # plt.subplot(132),plt.imshow(edges,cmap = 'gray')
#
#
# plt.subplot(132),plt.imshow(edges,cmap = 'gray')
#
# plt.title('Edge Image1'), plt.xticks([]), plt.yticks([])
# contours, _ = cv2.findContours(edges2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# for contour in contours:
#     rect = cv2.minAreaRect(contour)
#     box = cv2.boxPoints(rect)
#     box = np.int0(box)
#     cv2.drawContours(edges2, [box], 0, (0, 0, 255), 2)
# cv2.imshow('Image with bounding rectangles', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# plt.subplot(133),plt.imshow(edges2,cmap = 'gray')
# plt.title('Edge Image2'), plt.xticks([]), plt.yticks([])
# plt.show()


