---
layout: single
title: "Introduction to Lidar Raster Data Products"
excerpt: "This lesson introduces the raster geotiff file format - which is often used
to store lidar raster data. You learn the 3 key spatial attributes of a raster dataset
including Coordinate reference system, spatial extent and resolution."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['intro-lidar-raster-r']
permalink: /courses/earth-analytics/lidar-raster-data-r/open-lidar-raster-r/
nav-title: 'Open Raster Data R'
module-title: 'Lidar Raster Data R'
module-description: 'This module introduces the raster spatial data format as it
relates to working with lidar data in R. You will learn how to open, crop and classify raster data in
R. Also you will learn three commonly used lidar data products: the digital elevation model, digital surface model and the canopy height model.'
module-nav-title: 'Lidar Raster Data in R'
module-type: 'class'
week: 3
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: false
order: 1
class-order: 2
topics:
  reproducible-science-and-programming:
  remote-sensing: ['lidar']
  earth-science: ['vegetation']
  spatial-data-and-gis: ['raster-data']
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Open a lidar raster dataset in `R`.
* List and define 3 spatial attributes of a raster dataset: extent, `crs` and resolution.
* Identify the resolution of a raster in `R`.
* Plot a lidar raster dataset in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson.

If you have not already downloaded the week 3 data, please do so now.
[<i class="fa fa-download" aria-hidden="true"></i> Download week 3 data (~250 MB)](https://ndownloader.figshare.com/files/7446715){:data-proofer-ignore='' .btn }

</div>

In the last lesson, you reviewed the basic principles behind what a lidar raster
dataset is in `R` and how point clouds are used to derive the raster. In this lesson, you
will learn how to open and plot a lidar raster dataset in `R`. You will also learn
3 key attributes of a raster dataset:

1. Spatial resolution
2. Spatial extent
3. Coordinate reference system

<figure>
  <a href="{{ site.url }}/images/courses/earth-analytics/lidar-raster-data-r/gridding.gif">
  <img src="{{ site.url }}/images/courses/earth-analytics/lidar-raster-data-r/gridding.gif" alt="Animation Showing the general process of taking lidar point clouds and converting them to a Raster Format"></a>
  <figcaption>
  Animation that shows the general process of taking lidar point clouds and
  converting them to a Raster Format. Source: Tristan Goulden, NEON.
  </figcaption>
</figure>



## Open Raster Data in R

To work with raster data in `R`, you can use the `raster` and `rgdal` packages.


```r
# load libraries
library(raster)
library(rgdal)

# Make sure your working directory is set to  wherever your 'earth-analytics' dir is
# setwd("earth-analytics-dir-path-here")
```

You use the `raster("path-to-raster-here")` function to open a raster dataset in `R`.
Note that you use the `plot()` function to plot the data. The function argument
`main = ""` adds a title to the plot.











