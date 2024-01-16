import arcpy
mask = r"C:\Users\lenovo\Desktop\preprocess\mask\mask68_72.tif"
newenv = r"C:\Users\lenovo\Desktop\preprocess\Image_16bit_BGR"
outdir = r"C:\Users\lenovo\Desktop\preprocess\Image_16bit_BGR_resize"
envlist = [newenv]
arcpy.env.workspace = newenv
datasets = arcpy.ListRasters()


# 计数器
nums = 0

# =tif==tif==tif==tif==tif==tif==tif==tif==tif==tif==tif==tif==tif==tif==tif=
for i in datasets:
    in_raster = i
    output = outdir + "\\" + i[:-1]
    arcpy.gp.ExtractByMask_sa(in_raster, mask, output)
    nums += 1
    print(str(nums) + " finish!")

# # =png==png==png==png==png==png==png==png==png==png==png==png==png==png==png=
# for i in datasets:
#     in_raster = i
#     # print(i[:-3] + "tif")
#     output = outdir + "\\" + i[:-3] + "tif"
#     print(output)
#     arcpy.gp.ExtractByMask_sa(in_raster, mask, output)
#     print(output + " finish!")