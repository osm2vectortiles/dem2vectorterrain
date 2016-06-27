# https://gis.stackexchange.com/questions/146296/how-to-create-composite-hillshade

gdaldem hillshade $1 hillshades_0.tmp.tif -s 111120 -z 3 -az 0 -alt 45 -compute_edges
gdaldem hillshade $1 hillshades_45.tmp.tif -s 111120 -z 3 -az 45 -alt 45 -compute_edges
gdaldem hillshade $1 hillshades_90.tmp.tif -s 111120 -z 3 -az 90 -alt 45 -compute_edges
gdaldem hillshade $1 hillshades_135.tmp.tif -s 111120 -z 3 -az 135 -alt 45 -compute_edges
gdaldem hillshade $1 hillshades_180.tmp.tif -s 111120 -z 3 -az 180 -alt 45 -compute_edges
gdaldem hillshade $1 hillshades_225.tmp.tif -s 111120 -z 3 -az 225 -alt 45 -compute_edges
gdaldem hillshade $1 hillshades_270.tmp.tif -s 111120 -z 3 -az 270 -alt 45 -compute_edges
gdaldem hillshade $1 hillshades_315.tmp.tif -s 111120 -z 3 -az 315 -alt 45 -compute_edges
