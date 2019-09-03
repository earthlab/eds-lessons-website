---
layout: single
title: "Plot Grid of Spatial Plots in R. "
excerpt: "In this lesson you learn to use the par() or parameter settings in R to plot several raster RGB plots in R in a grid. "
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['how-to-hints-week8']
permalink: /courses/earth-analytics/multispectral-remote-sensing-modis/grid-of-plots-report/
nav-title: 'Grid of Plots'
week: 8
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 3
topics:
  reproducible-science-and-programming:
  data-exploration-and-analysis: ['data-visualization']
  spatial-data-and-gis: ['raster-data']
lang-lib:
  r: []
redirect_from:
  - "/courses/earth-analytics/week-7/grid-of-plots-report/" 
---

{% include toc title="In This Lesson" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Plot several plots using baseplot functions in a "grid" as one graphic in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data for week 8 of the course.

{% include /data_subsets/course_earth_analytics/_data-week6-7.md %}
</div>



```r
# load libraries
library(raster)
library(rgeos)
library(rgdal)
```













