---
layout: single
title: "Maps in R: R Maps Tutorial Using Ggplot"
excerpt: "You can use R as a GIS. Learn how to create a map in R using ggplot in this R maps tutorial."
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['hw-custom-maps-r']
permalink: /courses/earth-analytics/spatial-data-r/make-maps-with-ggplot-in-R/
nav-title: 'Maps with ggplot'
week: 4
course: "earth-analytics"
module-type: "class"
sidebar:
  nav:
author_profile: false
comments: false
order: 2
class-order: 2
topics:
  spatial-data-and-gis: ['vector-data', 'coordinate-reference-systems', 'maps-in-r']
  reproducible-science-and-programming:
redirect_from:
   - "/course-materials/earth-analytics/week-4/make-maps-with-ggplot-in-R/"
---

<!--# remove module-type: 'class' so it doesn't render live -->

{% include toc title="In This Lesson" icon="file-text" %}




<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Create a map in `R` using `ggplot()`.
* Plot a vector dataset by attributes in `R` using `ggplot()`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data for week 4 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 4 Data (~500 MB)](https://ndownloader.figshare.com/files/7525363){:data-proofer-ignore='' .btn }

</div>

## Making Maps with GGPLOT

In the previous lesson, you used base `plot()` to create a map of vector data -
your roads data - in `R`. In this lesson you will create the same maps, however
instead you will use `ggplot()`. `ggplot` is a powerful tool for making custom maps.
Compared to base plot, you will find creating custom legends to be simpler and cleaner,
and creating nicely formatted themed maps to be simpler as well.

However, you will have to convert your data from spatial (`sp`) objects to `data.frame`s
to use `ggplot`. The process isn't bad once you have the steps down! Let's check
it out.

<i class="fa fa-star"></i> **Data Tip:** If your data attribute values are not
read in as factors, you can convert the categorical
attribute values using `as.factor()`.
{: .notice--success}



First, let's import all of the needed libraries.


```r
# load libraries
library(raster)
library(rgdal)
library(ggplot2)
library(broom)
library(RColorBrewer)
library(rgeos)
library(dplyr)
# note that you don't need to call maptools to run the code below but it needs to be installed.
library(maptools)
# to add a north arrow and a scale bar to the map
library(ggsn)
# set factors to false
options(stringsAsFactors = FALSE)
```

Next, import and explore the data.






























































