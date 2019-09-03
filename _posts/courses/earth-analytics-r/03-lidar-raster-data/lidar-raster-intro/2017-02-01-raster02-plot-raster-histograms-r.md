---
layout: single
title: "Plot Histograms of Raster Values in R"
excerpt: "This lesson introduces the raster geotiff file format - which is often used
to store lidar raster data. You learn the 3 key spatial attributes of a raster dataset
including Coordinate reference system, spatial extent and resolution."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['intro-lidar-raster-r']
permalink: /courses/earth-analytics/lidar-raster-data-r/plot-raster-histograms-r/
nav-title: 'Plot raster histograms'
week: 3
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: false
order: 2
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

* Open raster data in `R`.
* Create a histogram of raster values in `R`.
* Draw information on raster attributes from a histogram.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson.

If you have not already downloaded the week 3 data, please do so now.
[<i class="fa fa-download" aria-hidden="true"></i> Download Week 3 Data (~250 MB)](https://ndownloader.figshare.com/files/7446715){:data-proofer-ignore='' .btn }

</div>

In the last lesson, you learned 3 key attributes of a raster dataset:

1. Spatial resolution
2. Spatial extent
3. Coordinate reference systems

In this lesson, you will learn how to use histograms to better understand the
distribution of your data.




## Open Raster Data in R

To work with raster data in `R`, you can use the `raster` and `rgdal` packages.
Remember you can use the `raster()` function to import the raster object into R.











