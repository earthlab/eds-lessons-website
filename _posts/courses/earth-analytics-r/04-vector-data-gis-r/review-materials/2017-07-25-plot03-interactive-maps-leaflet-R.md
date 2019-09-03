---
layout: single
title: "Make Interactive Maps with Leaflet R - GIS in R"
excerpt: "In this lesson you learn the steps to create a map in R using ggplot."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['hw-custom-maps-r']
permalink: /courses/earth-analytics/spatial-data-r/make-interactive-maps-with-leaflet-r/
nav-title: 'Interactive Leaflet Maps'
week: 4
course: "earth-analytics"
module-type: "class"
sidebar:
  nav:
author_profile: false
comments: false
order: 3
class-order: 2
topics:
  spatial-data-and-gis: ['vector-data', 'coordinate-reference-systems', 'maps-in-r']
  reproducible-science-and-programming:
---


<!--# remove module-type: 'class' so it doesn't render live -->

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Create an interactive map in `R` using `leaflet()`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data for week 4 of the course.

</div>


First, let's import all of the needed libraries.


```r
# load libraries
library(dplyr)
library(rgdal)
library(ggplot2)
library(leaflet)
# set factors to false
options(stringsAsFactors = FALSE)
```


## Interactive Maps with Leaflet

Static maps are useful for creating figures for reports and presentation. Sometimes,
however, you want to interact with your data. You can use the leaflet package for
R to overlay your data on top of interactive maps. You can think about it like
Google  maps with your data overlaid on top!

### What is Leaflet?

<a href="http://leafletjs.com" target="_blank">Leaflet</a> is an open-source `JavaScript` library that can be used to create mobile-friendly interactive maps.

Leaflet:

* Is designed with *simplicity*, *performance* and *usability* in mind.
* Has a beautiful, easy to use, and <a href="http://leafletjs.com/reference.html" target="_blank">well-documented API</a>.


The `leaflet` `R` package 'wraps' Leaflet functionality in an easy to use `R` package! Below, you can see some code that creates a basic web-map.


```r
map <- leaflet() %>%
  addTiles() %>%  # use the default base map which is OpenStreetMap tiles
  addMarkers(lng = 174.768, lat = -36.852,
             popup = "The birthplace of R")
map
```




<iframe title="Basic Map" width="80%" height="600" src="{{ site.url }}/example-leaflet-maps/birthplace_r.html" frameborder="0" allowfullscreen></iframe>


Next, import and explore the data.












