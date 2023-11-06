import cv2
import os


# # 获取目录下所有图片名
# filename = os.listdir(r"D:\Graduationproject\transunet_pytorch-main\dataset\train\mask")
# print(filename)
# # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
# base_dir = r"D:\Graduationproject\transunet_pytorch-main\dataset\train\mask"  # input
# new_dir = r"D:\Graduationproject\transunet_pytorch-main\dataset\train\mask -binary"  # output
# for img in filename:
#     name = img
#     path1 = os.path.join(base_dir, img)
#     print(path1)
#     cv2.imshow(path1)
#     img = cv2.imread(path1)
#     # print(img)
#     Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # cv2.imshow(Grayimg)
#     ret, thresh = cv2.threshold(Grayimg, 1, 255, cv2.THRESH_TOZERO_INV)
#     print(ret)
#     cv2.imwrite('img.png', thresh)
#
#     cv2.waitKey(0)
#     image = image.open('img.png')
#     # 有需要可对图像进行大小调整
#     # image = image.resize((350, 350),Image.ANTIALIAS)
#     path = os.path.join(new_dir, name)
#     image.save(path)


# import cv2

# base_dir = r"D:\Graduationproject\transunet_pytorch-main\dataset\train\mask_duofenlei"  # input
base_dir = r"D:\Graduationproject\transunet_pytorch-main\danzhang"  # input
new_dir = r"D:\Graduationproject\transunet_pytorch-main\dataset\train"  # output


# filename = os.listdir(r"D:\Graduationproject\transunet_pytorch-main\dataset\train\mask_duofenlei")
filename = os.listdir(r"D:\Graduationproject\transunet_pytorch-main\danzhang")

for img in filename:
    name = img
    print(filename)
    os.listdir()
    path1 = os.path.join(base_dir, img)

    # 读取图片
    image = cv2.imread(path1)
    image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 阈值处理
    retval, dst = cv2.threshold(image1, 1, 100, cv2.THRESH_BINARY)
    print(retval)
    print(dst)

    path = os.path.join(new_dir, name)
    cv2.imwrite(path,dst)

    # # 图像显示
    # cv2.imshow("image", image)
    # cv2.imshow("dst", dst)
    #
    # # 等待窗口
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()