# -*- coding: utf-8 -*-
import os
from osgeo import gdal
from tqdm import tqdm

dir_path = r"C:\Users\lenovo\Desktop\Image_16bit_BGRNir"
# dir_path = r"C:\Users\lenovo\Desktop\bgr"
old_file = os.listdir(dir_path)

for i in tqdm(old_file):
    old_name = os.path.join(dir_path, i)
    new_name = os.path.join(dir_path, i[3:])
    os.rename(old_name, new_name)

