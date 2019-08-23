---
layout: single
title: "The Fastest Way to Process Rasters in R"
excerpt: "."
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['spectral-data-fire-r']
permalink: /courses/earth-analytics/multispectral-remote-sensing-data/process-rasters-faster-in-R/
nav-title: 'Faster Raster Calculations'
week: 7
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 5
topics:
  reproducible-science-and-programming:
  spatial-data-and-gis: ['raster-data']
lang-lib:
  r: []
redirect_from:
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Calculate NDVI using NAIP multispectral imagery in `R`.
* Describe what a vegetation index is and how it is used with spectral remote sensing data.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data for week 7 of the course.

{% include /data_subsets/course_earth_analytics/_data-week6-7.md %}

</div>

Below you will find several benchmark tests that demonstrate the fastest way
to process raster data in R.

The summary:

1. For basic raster math - for example subtracting two rasters, it's fastest to
just perform the math!
2. For more complex math calculations like NDVI, the overlay function is faster.
3. Raster bricks are always faster!


```r
# load spatial packages
library(raster)
library(rgdal)
library(rgeos)
# turn off factors
options(stringsAsFactors = FALSE)
```














