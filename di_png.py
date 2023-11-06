import numpy as np
import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像

from PIL import Image
path1='D:/Graduation project/U-Net/lesson-2/test/.'
path='D:\Graduation project\已标注数据\scoliosis_cewan_png'

def nii_to_image(niifile):
    filenames = os.listdir(filepath)  # 读取nii文件夹
    slice_trans = []

    for f in filenames:
        # 开始读取nii文件
        img_path = os.path.join(filepath, f)
        img1 = nib.load(img_path)  # 读取nii
        img=nib.as_closest_canonical(img1)
        img_fdata = img.get_fdata()
        fname = f.replace('.nii', '')  # 去掉nii的后缀名
        img_f_path = os.path.join(imgfile, fname)
        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_f_path):
            os.mkdir(img_f_path)  # 新建文件夹

        # 开始转换为图像
        (x, y, z) = img.shape
        print(img.shape)
        for i in range(x):  # z是图像的序列
            silce = img_fdata[:,i:,]  # 选择哪个方向的切片都可以
            imageio.imwrite(os.path.join(img_f_path, '{}.png'.format(i)), silce)
            # img = Image.open(path+"/1chuli_reg.gz/"+str(i)+".png")
            #img = img.transpose(Image.ROTATE_90)
            #img.save(os.path.join(img_f_path, '{}.png'.format(i)))

            # 保存图像


if __name__ == '__main__':
    filepath = path1
    imgfile = path
    nii_to_image(filepath)