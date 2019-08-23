---
layout: single
title: "Clip Raster in R"
excerpt: "You can clip a raster to a polygon extent to save processing time and make image sizes smaller. Learn how to crop a raster dataset in R."
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['intro-lidar-raster-r']
permalink: /courses/earth-analytics/lidar-raster-data-r/crop-raster-data-in-r/
nav-title: 'Crop a Raster'
week: 3
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 6
topics:
  reproducible-science-and-programming:
  remote-sensing: ['lidar']
  earth-science: ['vegetation']
  spatial-data-and-gis: ['raster-data']
redirect_from:
   - "/course-materials/earth-analytics/week-3/crop-raster-data-in-r/"
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Crop a raster dataset in `R` using a vector extent object derived from a shapefile.
* Open a shapefile in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You need `R` and `RStudio` to complete this tutorial. Also you should have
an `earth-analytics` directory set up on your computer with a `/data`
directory with it.

* [How to set up R / RStudio](/courses/earth-analytics/document-your-science/setup-r-rstudio/)
* [Set up your working directory](/courses/earth-analytics/document-your-science/setup-working-directory/)
* [Intro to the R & RStudio interface](/courses/earth-analytics/document-your-science/intro-to-r-and-rstudio)

### R Libraries to Install:

* **raster:** `install.packages("raster")`
* **rgdal:** `install.packages("rgdal")`
* * **sf:** `install.packages("sf")`

If you have not already downloaded the week 3 data, please do so now.
[<i class="fa fa-download" aria-hidden="true"></i> Download Week 3 Data (~250 MB)](https://ndownloader.figshare.com/files/7446715){:data-proofer-ignore='' .btn }

</div>

In this lesson, you will learn how to crop a raster dataset in `R`. Previously,
you reclassified a raster in `R`, however the edges of your raster dataset were uneven.
In this lesson, you will learn how to crop a raster - to create a new raster
object / file that you can share with colleagues and / or open in other tools such
as `QGIS`.

## Load Libraries


```r
# load the raster and rgdal libraries
library(raster)
library(rgdal)
# if you want to use sf. you will use sf for future lessons!
```

## Open Raster and Vector Layers

First, you will use the `raster()` function to open a raster layer. Let's open the
canopy height model that you created in the previous lesson







