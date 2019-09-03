---
layout: single
title: "Import and Summarize Tree Height Data and Compare it to Lidar Derived Height in R"
excerpt: "It is important to compare differences between tree height measurements made by humans on the ground to those estimated using lidar remote sensing data. Learn how to perform this analysis and calculate error or uncertainty in R."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['remote-sensing-uncertainty-r']
permalink: /courses/earth-analytics/remote-sensing-uncertainty/import-summarize-tree-height-data/
nav-title: 'Compare Ground to Lidar Data'
week: 5
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 3
topics:
  remote-sensing: ['lidar']
  earth-science: ['vegetation', 'uncertainty']
  reproducible-science-and-programming:
  spatial-data-and-gis: ['vector-data', 'raster-data']
redirect_from:
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Use pipes to summarize tree height data by plot stored in `.csv` format.
* Merge a regular `data.frame` to a spatial `data.frame` object.
* Create scatterplots using `ggplot()` that compare 2 variables using a 1:1 line.

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

In the last lesson you extracted canopy height data at each field site location
from a NEON Canopy Height Model. In this lesson, you will summarize your field
site data so that you can compare tree heights measured on the ground with
tree heights derived from lidar data.

You will use the `dplyr` library to manipulate your data.

## Extract Descriptive Stats From *In situ* Data

First let's import and explore your tree height data. Note that your tree
height data is stored in `.csv` format. How many unique plots are in the data?



















