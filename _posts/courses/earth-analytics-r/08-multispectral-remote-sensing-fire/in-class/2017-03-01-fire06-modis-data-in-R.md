---
layout: single
title: "Work with MODIS Remote Sensing Data in R."
excerpt: "In this lesson you will explore how to import and work with MODIS remote sensing data in raster geotiff format in R. You will cover importing many files using regular expressions and cleaning raster stack layer names for nice plotting."
authors: ['Megan Cattau', 'Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['spectral-data-fire-2-r']
permalink: /courses/earth-analytics/multispectral-remote-sensing-modis/modis-data-in-R/
nav-title: 'MODIS Data in R'
week: 8
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 6
lang-lib:
  r: []
topics:
  remote-sensing: ['modis']
  earth-science: ['fire']
  spatial-data-and-gis: ['raster-data']
redirect_from:
  - "/courses/earth-analytics/week-7/modis-data-in-R/"
---



{% include toc title="In This Lesson" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Open MODIS imagery in `R`.
* Create NBR index using MODIS imagery in `R`.
* Calculate total burned area in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data for week 8 of the course.

{% include /data_subsets/course_earth_analytics/_data-week6-7.md %}
</div>




First, let's import MODIS data. Below notice that you have used a slightly different
version of the `list.files()` `pattern = ` argument.

You have used `glob2rx("*sur_refl*.tif$")` to select all layers that both

1. Contain the word `sur_refl` in them and
2. Contain the extension `.tif`

Let's import your MODIS image stack.










































