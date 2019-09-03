---
layout: single
title: "Extract Raster Values Using Vector Boundaries in R"
excerpt: "This lesson reviews how to extract pixels from a raster dataset using a
vector boundary. You can use the extracted pixels to calculate mean and max tree height for a study area (in this case a field site where tree heights were measured on the ground. Finally you will compare tree heights derived from lidar data compared to tree height measured by humans on the ground. "
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['remote-sensing-uncertainty-r']
permalink: /courses/earth-analytics/remote-sensing-uncertainty/extract-data-from-raster/
nav-title: 'Extract Data From Raster'
week: 5
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 2
topics:
  remote-sensing: ['lidar']
  earth-science: ['vegetation', 'uncertainty']
  reproducible-science-and-programming:
  spatial-data-and-gis: ['vector-data', 'raster-data']
redirect_from:
   - "/course-materials/earth-analytics/week-5/extract-data-from-raster/"
   - "/courses/earth-analytics/week-5/extract-data-from-raster/"
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Use the `extract()` function to extract raster values using a vector extent or set of extents.
* Create a scatter plot with a one-to-one line in `R`.
* Understand the concept of uncertainty as it's associated with remote sensing data.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data for week 4 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 4 Data (~500 MB)](https://ndownloader.figshare.com/files/7525363){:data-proofer-ignore='' .btn }

</div>




```r
# load libraries
library(raster)
library(rgdal)
library(rgeos)
library(ggplot2)
library(dplyr)

options(stringsAsFactors = FALSE)

# set working directory
# setwd("path-here/earth-analytics")
```

## Import Canopy Height Model

First, you will import a canopy height model created by the NEON project. In the
previous lessons / weeks you learned how to make a canopy height model by
subtracting the digital elevation model (`DEM`) from the digital surface model (`DSM`).














