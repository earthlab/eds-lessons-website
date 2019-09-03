---
layout: single
title: "Clean Remote Sensing Data in R - Clouds, Shadows & Cloud Masks"
excerpt: "In this lesson, you will learn how to deal with clouds when working with spectral remote sensing data. You will learn how to mask clouds from landsat and MODIS remote sensing data in R using the mask() function. You will also discuss issues associated with cloud cover - particular as they relate to a research topic."
authors: ['Leah Wasser','Megan Cattau']
modified: '2019-09-03'
category: [courses]
class-lesson: ['spectral-data-fire-2-r']
permalink: /courses/earth-analytics/multispectral-remote-sensing-modis/intro-spectral-data-r/
nav-title: 'Clouds, Shadows & Masks'
module-title: 'Clouds, shadows & cloud masks in R'
module-description: 'In this module you will learn more about dealing with clouds, shadows and other elements that can interfere with scientific analysis of remote sensing data. '
module-nav-title: 'Fire / spectral remote sensing data - in R'
module-type: 'class'
class-order: 1
course: "earth-analytics"
week: 8
sidebar:
  nav:
author_profile: false
comments: true
order: 1
topics:
  remote-sensing: ['landsat', 'modis']
  earth-science: ['fire']
  reproducible-science-and-programming:
  spatial-data-and-gis: ['raster-data']
lang-lib:
  r: []
redirect_from:
  - "/courses/earth-analytics/week-7/intro-spectral-data-r/"
---


{% include toc title="In This Lesson" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Describe the impacts that thick cloud cover can have on analysis of remote sensing data.
* Use a cloud mask to remove portions of an spectral dataset (image) that is covered by clouds / shadows.
* Define cloud mask / describe how a cloud mask can be useful when working with remote sensing data.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data that you already downloaded for week 8 of the course.

{% include /data_subsets/course_earth_analytics/_data-week6-7.md %}

</div>

## About Landsat Scenes

Landsat satellites orbit the earth continuously collecting images of the Earth's
surface. These images, are divided into smaller regions - known as scenes.

> Landsat images are usually divided into scenes for easy downloading. Each
> Landsat scene is about 115 miles long and 115 miles wide (or 100 nautical
> miles long and 100 nautical miles wide, or 185 kilometers long and 185 kilometers wide). -*wikipedia*


### Challenges Working with Landsat Remote Sensing Data
In the previous lessons, you learned how to import a set of geotiffs that made
up the bands of a landsat raster. Each geotiff file was a part of a Landsat scene,
that had been downloaded for this class by your instructor. The scene was further
cropped to reduce the file size for the class.

You ran into some challenges when you began to work with the data. The biggest
problem was a large cloud and associated shadow that covered your study
area of interest - the Cold Springs fire burn scar.

### Dealing with Clouds & Shadows in Remote Sensing Data

Clouds and atmospheric conditions present a significant challenge when working
with multispectral remote sensing data. Extreme cloud cover and shadows can make
the data in those areas, un-usable given reflectance values are either washed out
(too bright - as the clouds scatter all light back to the sensor) or are too
dark (shadows which represent blocked or absorbed light).

In this lesson you will learn how to deal with clouds in your remote sensing data.
There is no perfect solution of course. You will just learn one approach.

Begin by loading your spatial libraries.


```r
# import spatial packages
library(raster)
library(rgdal)
library(rgeos)
# turn off factors
options(stringsAsFactors = FALSE)
```

Next, you will load the landsat bands that you loaded previously in your homework.



















