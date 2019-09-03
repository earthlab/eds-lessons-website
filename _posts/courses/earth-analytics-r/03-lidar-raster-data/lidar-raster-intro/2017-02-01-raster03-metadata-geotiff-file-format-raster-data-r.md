---
layout: single
title: "How to Open and Use Files in Geotiff Format"
excerpt: "A GeoTIFF is a standard file format with spatial metadata embedded as tags. Use the raster package in R to open geotiff files and spatial metadata programmatically."
authors: ['Leah Wasser', 'NEON Data Skills']
modified: '2019-09-03'
category: [courses]
class-lesson: ['intro-lidar-raster-r']
permalink: /courses/earth-analytics/lidar-raster-data-r/introduction-to-spatial-metadata-r/
nav-title: 'Intro to the Geotiff'
week: 3
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: false
order: 3
topics:
  reproducible-science-and-programming:
  spatial-data-and-gis: ['raster-data']
  find-and-manage-data: ['metadata']
redirect_from:
   - "/course-materials/earth-analytics/week-3/introduction-to-spatial-metadata-r/"
---


{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Access metadata stored within a `geotiff` raster file via tif tags in `R`.
* Describe the difference between embedded metadata and non embedded metadata.
* Use `GDALinfo()` to quickly view key spatial metadata attributes associated with a spatial file.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson.

If you have not already downloaded the week 3 data, please do so now.
[<i class="fa fa-download" aria-hidden="true"></i> Download Week 3 Data (~250 MB)](https://ndownloader.figshare.com/files/7446715){:data-proofer-ignore='' .btn }

</div>



## What is a GeoTIFF??

A GeoTIFF is a standard `.tif` or image file format that includes additional spatial
(georeferencing) information embedded in the .tif file as tags. These are called embedded
tags, `tif tags`. These tags can include the following raster metadata:

1. **Spatial Extent:** What area does this dataset cover?
2. **Coordinate reference system:** What spatial projection / coordinate reference
system is used to store the data? Will it line up with other data?
3. **Resolution:** The data appears to be in **raster** format. This means it is
composed of pixels. What area on the ground does each pixel cover - i.e. What is
its spatial resolution?
4. **No data value**
5. **Layers:** How many layers are in the .tif file. (more on that later)

You learned spatial extent and resolution in the previous lesson. When you work with
`geotiff`s the spatial information that describes the raster data are embedded within
the file itself.

<i class="fa fa-star"></i> **Data note:**  Your camera uses embedded tags to store
information about pictures that you take including the camera make and model,
and the time the image was taken.
{: .notice--success }

More about the  `.tif` format:

* <a href="https://en.wikipedia.org/wiki/GeoTIFF" target="_blank"> GeoTIFF on Wikipedia</a>
* <a href="https://trac.osgeo.org/geotiff/" target="_blank"> OSGEO TIFF documentation</a>

### Geotiffs in R

The `raster` package in `R` allows us to both open `geotiff` files and also directly
access `.tif tags` programmatically. You can quickly view the spatial **extent**,
**coordinate reference system** and **resolution** of your raster data.

NOTE: not all `geotiff`s contain `tif` tags!

You can use `GDALinfo()` to view all of the relevant tif tags embedded within a
`geotiff` before you open it in `R`.













