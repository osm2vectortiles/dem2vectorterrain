# dem2vectorterrain

> UPDATE: vector tiles made from a terrain are available at https://openmaptiles.com/contours/. The software for turning raster data into bezier curves and polygons is available as a service via https://octogeo.com/.

This is an exploration of converting DEMs to vector hillshades and contours for inclusion into osm2vectortiles

Thoughts:

1. Use ASTER DEMs. Superior to SRTM and openly available (but do see their license), see http://www.digital-geography.com/dem-comparison-srtm-3-vs-aster-gdem-v2/ for a comparison.
2. Export to hillshade with gdaldem (http://www.gdal.org/gdaldem.html)
   - Export the hillshade to contours using gdal_contour (http://www.gdal.org/gdal_contour.html) (See https://www.mapbox.com/vector-tiles/mapbox-terrain/ and https://github.com/mapbox/mapbox-gl-styles/blob/outdoors-v8/styles/outdoors-v8.json for an example of how to make compatible with existing styles) Use gdal_contour over gdalpolygonize as we don't need all the values in shapefiles, just general contours to match discrete hillshade values
   - Import these hillshade polygons into postgres
   - Convert contour lines to polygons in postgis (Dissolve on elevation and ST_MakePolygon)
   - Generalize for other layers (remove vertices and perhaps in between hillshades depending on density)
3. Export to contours with gdal_contour (http://www.gdal.org/gdal_contour.html) (what elevation resolution?)
   - Import these contours into postgres
   - Generalize for other layers (remove vertices and perhaps in between elevations depending on density)
6. Dockerize to the following stages:
   - export hillshade to vectors in postgres (import-hillshade), generalize vectors (generalize-hillshade) 
   - export to contours in postgres (import-contours), generalize vectors (generalize-contours)
   - Both are done on a per-tile basis for imports
   - Exports integrated into osm2vectortiles
   - Undecided on whether to merge features in postgres so intersecting contours of same elevation are dissolved by elevation attribute 
7. Need a tm2 source, integrated into osm2vectortiles?
