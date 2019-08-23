---
layout: single
title: "Calculate NDVI in R: Remote Sensing Vegetation Index"
excerpt: "NDVI is calculated using near infrared and red wavelengths or types of light and is used to measure vegetation greenness or health. Learn how to calculate remote sensing NDVI using multispectral imagery in R."
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['spectral-data-fire-r']
permalink: /courses/earth-analytics/multispectral-remote-sensing-data/vegetation-indices-NDVI-in-R/
nav-title: 'Calculate NDVI NAIP'
week: 7
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 4
topics:
  remote-sensing: ['landsat', 'modis']
  earth-science: ['fire']
  reproducible-science-and-programming:
  spatial-data-and-gis: ['raster-data']
lang-lib:
  r: []
redirect_from:
   - "/course-materials/earth-analytics/week-6/vegetation-indices-NDVI-in-R/"
   - "/courses/earth-analytics/week-6/vegetation-indices-NDVI-in-R/"
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

## About Vegetation Indices

A vegetation index is a single value that quantifies vegetation health or structure.
The math associated with calculating a vegetation index is derived from the physics
of light reflection and absorption across bands. For instance, it is known that
healthy vegetation reflects light strongly in the near infrared band and less strongly
in the visible portion of the spectrum. Thus, if you create a ratio between light
reflected in the near infrared and light reflected in the visible spectrum, it
will represent areas that potentially have healthy vegetation.


## Normalized Difference Vegetation Index (NDVI)

The Normalized Difference Vegetation Index (NDVI) is a quantitative index of
greenness ranging from 0-1, where 0 represents minimal or no greenness and 1
represents maximum greenness.

NDVI is often used for a quantitate proxy measure of vegetation health, cover
and phenology (life cycle stage) over large areas.

<figure>
 <a href="{{ site.url }}/images/courses/earth-analytics/remote-sensing/nasa-earth-observatory-ndvi-diagram.jpg">
 <img src="{{ site.url }}/images/courses/earth-analytics/remote-sensing/nasa-earth-observatory-ndvi-diagram.jpg" alt="NDVI image from NASA that shows reflectance."></a>
    <figcaption>NDVI is calculated from the visible and near-infrared light
    reflected by vegetation. Healthy vegetation (left) absorbs most of the
    visible light that hits it, and reflects a large portion of
    near-infrared light. Unhealthy or sparse vegetation (right) reflects more
    visible light and less near-infrared light. Source: NASA Earth Observatory
    </figcaption>
</figure>

* <a href="http://earthobservatory.nasa.gov/Features/MeasuringVegetation/measuring_vegetation_2.php" target="_blank">
More on NDVI from NASA</a>

## Calculate NDVI in R

Sometimes you can download already calculated NDVI data products. In this
case, you need to calculate NDVI using the NAIP imagery / reflectance data that you have.



```r
# load spatial packages
library(raster)
library(rgdal)
library(rgeos)
library(RColorBrewer)

# turn off factors
options(stringsAsFactors = FALSE)
```

























