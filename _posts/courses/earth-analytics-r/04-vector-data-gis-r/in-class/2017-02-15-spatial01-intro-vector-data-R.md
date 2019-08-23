---
layout: single
title: "GIS in R: Intro to Vector Format Spatial Data - Points, Lines and Polygons"
excerpt: "This lesson introduces what vector data are and how to open vector data stored in
shapefile format in R. "
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['class-intro-spatial-r']
permalink: /courses/earth-analytics/spatial-data-r/intro-vector-data-r/
nav-title: 'Vector Data in R'
module-title: 'Spatial Data in R and Remote Sensing Uncertainty'
module-description: 'This tutorial covers the basic principles of LiDAR remote sensing and
the three commonly used data products: the digital elevation model, digital surface model and the canopy height model. Finally it walks through opening lidar derived raster data in R / RStudio'
module-nav-title: 'Spatial Data in R'
module-type: 'class'
course: "earth-analytics"
week: 4
sidebar:
  nav:
author_profile: false
comments: true
order: 1
topics:
  spatial-data-and-gis: ['vector-data', 'coordinate-reference-systems']
  reproducible-science-and-programming:
redirect_from:
  - "/course-materials/earth-analytics/week-4/intro-vector-data-r/"
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Describe the characteristics of 3 key vector data structures: points, lines and polygons.
* Open a shapefile in R using `readOGR()`.
* View the metadata of a vector spatial layer in R including CRS.
* Access the tabular (`data.frame`) attributes of a vector spatial layer in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data for week 4 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 4 Data (~500 MB)](https://ndownloader.figshare.com/files/7525363){:data-proofer-ignore='' .btn }

</div>

## About Vector Data
Vector data are composed of discrete geometric locations (x,y values) known as
**vertices** that define the "shape" of the spatial object. The organization
of the vertices determines the type of vector that you are working
with: point, line or polygon.

<figure>
    <a href="{{ site.url }}/images/courses/earth-analytics/spatial-data/points-lines-polygons-vector-data-types.png">
    <img src="{{ site.url }}/images/courses/earth-analytics/spatial-data/points-lines-polygons-vector-data-types.png" alt="points lines and polygons graphic."></a>
    <figcaption> There are 3 types of vector objects: points, lines or
    polygons. Each object type has a different structure.
    Image Source: Colin Williams (NEON)
    </figcaption>
</figure>

* **Points:** Each individual point is defined by a single x, y coordinate.
There can be many points in a vector point file. Examples of point data include:
sampling locations, the location of individual trees or the location of plots.
* **Lines:** Lines are composed of many (at least 2) vertices, or points, that
are connected. For instance, a road or a stream may be represented by a line. This
line is composed of a series of segments, each "bend" in the road or stream
represents a vertex that has defined `x, y` location.
* **Polygons:** A polygon consists of 3 or more vertices that are connected and
"closed". Thus the outlines of plot boundaries, lakes, oceans, and states or
countries are often represented by polygons. Occasionally, a polygon can have a
hole in the middle of it (like a doughnut), this is something to be aware of but
not an issue you will deal with in this tutorial.

<i class="fa fa-star"></i> **Data Tip:** Sometimes boundary layers such as
states and countries, are stored as lines rather than polygons. However, these
boundaries, when represented as a line, will not create a closed object with a
defined "area" that can be "filled".
{: .notice--success}

## Shapefiles: Points, Lines, and Polygons
Geospatial data in vector format are often stored in a shapefile format.
Because the structure of points, lines, and polygons are different, each
individual shapefile can only contain one vector type (all points, all lines
or all polygons). You will not find a mixture of point, line and polygon
objects in a single shapefile.

Objects stored in a shapefile often have a set of associated `attributes` that
describe the data. For example, a line shapefile that contains the locations of
streams, might contain the associated stream name, stream "order" and other
information about each stream line object.

* More about shapefiles can found on
<a href="https://en.wikipedia.org/wiki/Shapefile" target="_blank">Wikipedia</a>.

## Import Shapefiles

You will use the `rgdal` package to work with vector data in `R`. Notice that the
`sp` package automatically loads when `rgdal` is loaded. You will also load the
`raster` package so you can explore raster and vector spatial metadata using similar commands.


```r
# work with spatial data; sp package will load with rgdal.
library(rgdal)
library(rgeos)
# for metadata/attributes- vectors or rasters
library(raster)

# set working directory to earth-analytics dir
# setwd("pathToDirHere")
```

The shapefiles that you will import are:

* A polygon shapefile representing your field site boundary.
* A line shapefile representing roads.
* A point shapefile representing the location of field sites located at the
<a href="http://www.neonscience.org/science-design/field-sites/harvard-forest" target="_blank"> San Joachin field site</a>.

The first shapefile that you will open contains the point locations where trees
have been measured at the study site. The data are stored in shapefile format.
To import shapefiles you use the `R` function `readOGR()`.

`readOGR()` requires two components:

1. The directory where your shapefile lives: `data/week-04/california/SJER/vector_data/`.
2. The name of the shapefile (without the extension): `SJER_plot_centroids`.

You can call each element separately

`readOGR("path","fileName")`

Or you can simply include the entire path to the shp file in the path argument.
Both ways to open a shapefile are demonstrated below:















