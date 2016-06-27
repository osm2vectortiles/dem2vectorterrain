# Do not use this for anything, it's garbage code. Just to demo merging multiple hillshades (8-directions)
# Run this python script, with each of the 8 hillshades as input. This needs to be improved.
from osgeo import gdal
from osgeo.gdalnumeric import *
from osgeo.gdalconst import *
import sys

F1 = sys.argv[1]
F2 = sys.argv[2]
F3 = sys.argv[3]
F4 = sys.argv[4]
F5 = sys.argv[5]
F6 = sys.argv[6]
F7 = sys.argv[7]
F8 = sys.argv[8]

outFile = "out.tiff"

#Open the dataset
ds1 = gdal.Open(F1, GA_ReadOnly )
ds2 = gdal.Open(F2, GA_ReadOnly )
ds3 = gdal.Open(F3, GA_ReadOnly )
ds4 = gdal.Open(F4, GA_ReadOnly )
ds5 = gdal.Open(F5, GA_ReadOnly )
ds6 = gdal.Open(F6, GA_ReadOnly )
ds7 = gdal.Open(F7, GA_ReadOnly )
ds8 = gdal.Open(F8, GA_ReadOnly )

band1 = ds1.GetRasterBand(1)
band2 = ds2.GetRasterBand(1)
band3 = ds3.GetRasterBand(1)
band4 = ds4.GetRasterBand(1)
band5 = ds5.GetRasterBand(1)
band6 = ds6.GetRasterBand(1)
band7 = ds7.GetRasterBand(1)
band8 = ds8.GetRasterBand(1)

#Read the data into numpy arrays
data1 = BandReadAsArray(band1)
data2 = BandReadAsArray(band2)
data3 = BandReadAsArray(band3)
data4 = BandReadAsArray(band4)
data5 = BandReadAsArray(band5)
data6 = BandReadAsArray(band6)
data7 = BandReadAsArray(band7)
data8 = BandReadAsArray(band8)

#The actual calculation
dataOut = data1*0.125+data2*0.125+data3*0.125+data4*0.125+data5*0.125+data6*0.125+data7*0.125+data8*0.125

#Write the out file
driver = gdal.GetDriverByName("GTiff")
dsOut = driver.Create("out.tiff", ds1.RasterXSize, ds1.RasterYSize, 1, band1.DataType)
CopyDatasetInfo(ds1,dsOut)
bandOut=dsOut.GetRasterBand(1)
BandWriteArray(bandOut, dataOut)
