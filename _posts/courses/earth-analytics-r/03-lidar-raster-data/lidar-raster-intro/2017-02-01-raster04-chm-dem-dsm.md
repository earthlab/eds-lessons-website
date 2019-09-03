---
layout: single
title: "Create a Canopy Height Model With Lidar Data"
excerpt: "A canopy height model contains height values trees and can be used to understand landscape change over time. Learn how to use LIDAR elevation data to calculate canopy height and change in terrain over time."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['intro-lidar-raster-r']
permalink: /courses/earth-analytics/lidar-raster-data-r/lidar-chm-dem-dsm/
nav-title: 'CHM, DSM, DEM'
week: 3
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 4
topics:
  reproducible-science-and-programming:
  remote-sensing: ['lidar']
  earth-science: ['vegetation']
  spatial-data-and-gis: ['raster-data']
redirect_from:
   - "/course-materials/earth-analytics/week-3/lidar-chm-dem-dsm/"
---

{% include toc title="In This Lesson" icon="file-text" %}




<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Define Canopy Height Model (`CHM`), Digital Elevation Model (`DEM`) and Digital Surface Model (`DSM`).
* Describe the key differences between the **CHM**, **DEM**, **DSM**.
* Derive a **CHM** in `R` using raster math.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You need `R` and `RStudio` to complete this tutorial. Also you should have
an `earth-analytics` directory set up on your computer with a `/data`
directory with it.

* [How to set up R / RStudio](/courses/earth-analytics/document-your-science/setup-r-rstudio/)
* [Set up your working directory](/courses/earth-analytics/document-your-science/setup-working-directory/)
* [Intro to the R & RStudio interface](/courses/earth-analytics/document-your-science/intro-to-r-and-rstudio)

### R Libraries to iInstall:

* **raster:** `install.packages("raster")`
* **rgdal:** `install.packages("rgdal")`

If you have not already downloaded the week 3 data, please do so now.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 3 Data (~250 MB)](https://ndownloader.figshare.com/files/7446715){:data-proofer-ignore='' .btn }

</div>

As you learned in the previous lesson, lidar or **Li**ght **D**etection **a**nd
**R**anging is an active remote sensing system that can be used to measure
vegetation height across wide areas. If the data are discrete return, lidar point
clouds are most commonly derived data product from a lidar system. However, often
people work with lidar data in raster format given it's smaller in size and
thus easier to work with. In this lesson, you will import and work with
3 of the most common lidar derived data products in `R`:

1. **Digital Terrain Model (or DTM):** ground elevation or the elevation of the Earth's surface (sometimes also called a `DEM` or digital elevation model).
2. **Digital Surface Model (or DSM):** top of the surface (imagine draping a sheet over the canopy of a forest
3. **Canopy Height Model (CHM):** The height of objects above the ground.

## Three Important Lidar Data Products: CHM, DEM, DSM

<figure>
   <a href="{{ site.url }}/images/courses/earth-analytics/lidar-raster-data-r/lidarTree-height.png">
   <img src="{{ site.url }}/images/courses/earth-analytics/lidar-raster-data-r/lidarTree-height.png" alt="Lidar derived DSM, DTM and CHM."></a>
   <figcaption>Digital Surface Model (DSM), Digital Elevation Models (DEM) and
   the Canopy Height Model (CHM) are the most common raster format lidar
   derived data products. One way to derive a CHM is to take
   the difference between the digital surface model (DSM, tops of trees, buildings
   and other objects) and the Digital Terrain Model (DTM, ground level). The CHM
   represents the actual height of trees, buildings, etc. with the influence of
   ground elevation removed. Graphic: Colin Williams, NEON
   </figcaption>
</figure>


### Digital Elevation Model
In the previous lesson, you opened a digital elevation model. The digital elevation
model (`DEM`), also known as a digital terrain model (`DTM`) represents the elevation
of the Earth's surface. The `DEM` represents the ground - and thus DOES NOT INCLUDE
trees and buildings and other objects.



```r
# load libraries
library(raster)
library(rgdal)

# set working directory to ensure R can find the file you wish to import
# setwd("working-dir-path-here")
```

First, let's open and plot the digital elevation model.











