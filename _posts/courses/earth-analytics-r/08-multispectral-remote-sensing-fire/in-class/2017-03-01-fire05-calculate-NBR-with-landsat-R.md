---
layout: single
title: "Calculate and Plot Difference Normalized Burn Ratio (dNBR) from Landsat Remote Sensing Data in R"
excerpt: "In this lesson you review how to calculate difference normalized burn ratio using pre and post fire NBR rasters in R. You finally will classify the dNBR raster."
authors: ['Leah Wasser','Megan Cattau']
modified: '2019-09-03'
category: [courses]
class-lesson: ['spectral-data-fire-2-r']
permalink: /courses/earth-analytics/multispectral-remote-sensing-modis/calculate-dNBR-R-Landsat/
nav-title: 'dNBR With Landsat'
class-order: 3
week: 8
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 5
topics:
  remote-sensing: ['landsat', 'modis']
  earth-science: ['fire']
  reproducible-science-and-programming:
  spatial-data-and-gis: ['raster-data']
lang-lib:
  r: []
redirect_from:
   - "/courses/earth-analytics/week-6/calculate-dNBR-R-Landsat/"
   - "/courses/earth-analytics/spectral-remote-sensing-landsat/calculate-dNBR-R-Landsat/"

---

{% include toc title="In This Lesson" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Calculate `dNBR` in `R` with Landsat data.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data for week 8 of the course.

{% include /data_subsets/course_earth_analytics/_data-week6-7.md %}
</div>

As discussed in the previous lesson, you can use dNBR to map the extent and
severity of a fire. In this lesson, you learn how to create NBR using
Landsat data.

You calculate dNBR using the following steps:

1. Open up pre-fire data and calculate *NBR*
2. Open up the post-fire data and calculate *NBR*
3. Calculate **dNBR** (difference NBR) by subtracting post-fire NBR from pre-fire NBR (NBR pre - NBR post fire).
4. Classify the dNBR raster using the classification table provided below and isn the previous lesson.

Note the code to do this is hidden. You will need to figure
out what bands are required to calculate NBR using Landsat.

## Calculate dNBR Using Landsat Data

First, let's setup your spatial packages.


```r
# load spatial packages
library(raster)
library(rgdal)
library(rgeos)
library(RColorBrewer)
library(dplyr)

# turn off factors
options(stringsAsFactors = FALSE)

# source the normalized diff function that you write for week_7
#source("ea-course-functions.R")
```



Next, open up the pre- Cold Springs fire Landsat data. Create a rasterbrick from the bands. Then calculate NBR. A plot of NBR is below.

































