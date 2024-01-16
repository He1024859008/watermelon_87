# -*- coding: utf-8 -*-
import os
from osgeo import gdal
from tqdm import tqdm

def bands_select(img_path):
    '''
    实现遥感影像的波段重组
    :param img_path:
    :return:
    '''
    # 读取影像信息
    img_array, img_proj, img_geotrans, datatype = img_read(img_path)
    # 波段选择，这里是去掉最后一个波段
    dst_array = img_array[:img_array.shape[0] - 1]
    dst_path = os.path.join(os.path.dirname(img_path), 'rs_' + os.path.basename(img_path))
    # 写入修改后的影像
    img_write(dst_path, dst_array, img_proj, img_geotrans, datatype)
    print(dst_path, 'get!')


def img_read(img_path):
    '''
    读取遥感影像，返回 影像栅格矩阵、影像投影、影像仿射矩阵、影像数据类型  信息
    :param img_path:
    :return:
    '''
    dataset = gdal.Open(img_path)
    img_width, img_height = dataset.RasterXSize, dataset.RasterYSize  # 栅格矩阵的行、列数
    img_geotrans = dataset.GetGeoTransform()  # 仿射矩阵
    img_proj = dataset.GetProjection()  # 地图投影信息
    img_array = dataset.ReadAsArray(0, 0, img_width, img_height)  # 将数据写成数组，对应栅格矩阵
    if 'int8' in img_array.dtype.name:
        datatype = gdal.GDT_Byte
    elif 'int16' in img_array.dtype.name:
        datatype = gdal.GDT_UInt16
    else:
        datatype = gdal.GDT_Float32
    return img_array, img_proj, img_geotrans, datatype


def img_write(img_path, img_array, img_proj, img_geotrans, datatype):
    '''
    输入，数据信息，写入影像文件
    :param img_path:
    :param img_array:
    :param img_proj:
    :param img_geotrans:
    :param datatype:
    :return:
    '''
    assert len(img_array.shape) == 3
    driver = gdal.GetDriverByName("GTiff")  # 创建文件驱动
    dataset = driver.Create(img_path, img_array.shape[2], img_array.shape[1], img_array.shape[0], datatype,
                            options=['COMPRESS=LZW'])
    # other options: 'BigTIFF=YES', 'TILED=YES',"INTERLEAVE=PIXEL",'COMPRESS=PACKBITS'

    dataset.SetGeoTransform(img_geotrans)  # 写入仿射变换参数
    dataset.SetProjection(img_proj)  # 写入投影
    for index, band in enumerate(img_array):
        dataset.GetRasterBand(index + 1).WriteArray(band)



# bands_select(img_path)

dir_path = r"C:\Users\lenovo\Desktop\Image_16bit_BGRNir"
# dir_path = r"C:\Users\lenovo\Desktop\bgr"
# list to store files
tif_name = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        tif_name.append(os.path.join(dir_path, path))
print("路径测试：", tif_name[0])
print("影像数量：", len(tif_name))
for i in tqdm(tif_name):
    bands_select(i)
    # print("finish!")

