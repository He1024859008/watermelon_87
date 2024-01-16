# -*- coding: utf-8 -*-
import os
from osgeo import gdal
from tqdm import tqdm


def check_size(dir_path):

    tif_name = []
    tif_size = {}

    for path in tqdm(os.listdir(dir_path), "Checking_size"):
        if os.path.isfile(os.path.join(dir_path, path)):
            # tif_name.append(os.path.join(dir_path, path))
            img_path = os.path.join(dir_path, path)
            dataset = gdal.Open(img_path)
            img_size = (dataset.RasterXSize,
                   dataset.RasterYSize,
                   dataset.RasterCount)

            tif_size[str(path)] = img_size

    return tif_size

# path = r"C:\Users\lenovo\Desktop\GID5-data\ann_dir\train"
Image_path = r"C:\Users\lenovo\Desktop\preprocess\Annotation__5index_tif"

sizes_list = check_size(Image_path)
for image in sizes_list:
    # print(image, sizes_list[image])

    # if sizes_list[image] == (7300, 6900, 3):  # 检查Image
    if sizes_list[image] == (7300, 6900, 1):  # 检查标签
        pass
    else:
        print(image, "size error!")
print("checking finished!")