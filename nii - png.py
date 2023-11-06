# noinspection PyUnresolvedReferences
import numpy as np
import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
import cv2


# noinspection PyUnusedLocal
def nii_to_image(niifile):

    filenames = os.listdir(filepath)  # 读取nii文件夹
    slice_trans = []

    for f in filenames:
        # 开始读取nii文件
        img_path = os.path.join(filepath, f)
        img = nib.load(img_path)  # 读取nii
        label_array = img.get_fdata()
        print(f'With the unique values: {np.unique(label_array)}')
        print(np.unique(label_array, return_counts=True))

        print("执行到这里2")

        pixdim = img.header['pixdim']
        print(f'z轴分辨率： {pixdim[3]}')
        print(f'in plane 分辨率： {pixdim[1]} * {pixdim[2]}')

        img_fdata = img.get_fdata()    #这里数据的存储方式？
        type(img_fdata)  # 数据存储方式为
        print(f'Type of the image {type(img_fdata)}')  # numpy数据类型ndarray   ndarry类型方便计算

        fname = f.replace('.nii', '')  # 去掉nii的后缀名
        img_f_path = os.path.join(imgfile, fname)
        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_f_path):
            os.mkdir(img_f_path)  # 新建文件夹
        x, y, z = img.shape  # 获取nii文件的三个维度大小`img.shape`返回一个元组（tuple）`(x, y, z)`，表示该三维图像数据的尺寸或形状，其中`x`表示第一维度（通常是行）、`y`表示第二维度（通常是列），而`z`表示第三维度（通常是深度或层数）
        print(f"The image object height: {y}, width:{x}, depth:{z}")#说明读取的是横的图片，所以后面要进行转置，深度读取出来是1
        silce = img_fdata[:, :, 0].transpose()  # 获取当前2维切片数据，并转置以匹配颜色映射表的形状，深度是1，所以取0







        pred = np.array(silce, np.uint8)
        # cv2.imshow("yuantu", color_silce)
        # cv2.waitKey(0)

        imageio.imwrite(os.path.join(img_f_path, '{}.png'.format(1)), silce)







        # 开始转换为图像
        # (x, y, z) = img.shape
        # for i in range(z):  # z是图像的序列
        #     silce = img_fdata[:, :, i]  # 选择哪个方向的切片都可以
        #     print(silce)
        #     imageio.imwrite(os.path.join(img_f_path, '{}.png'.format(i)), silce)
            # 保存图像

            #0-17             255怎么出来的
            #把0-17扩展成0-255 255chu

            #nill文件格式说明，示例代码，把nill存储格式  相应的代码
            #文件头图像数据  把silce 转换成三个通道 在每个通道上面做转换，不用imwrite


if __name__ == '__main__':
    filepath = 'D:/Graduation project/U-Net/lesson-2/test/.'
    imgfile = 'D:\Graduation project\已标注数据\scoliosis_cewan_png'
    nii_to_image(filepath)
