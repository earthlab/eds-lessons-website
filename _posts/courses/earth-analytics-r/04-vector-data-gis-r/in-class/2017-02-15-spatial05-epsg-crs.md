---
layout: single
title: "GIS in R: Understand EPSG, WKT and other CRS definition styles"
excerpt: "This lesson discusses ways that coordinate reference system data are stored including  proj4, well known text (wkt) and EPSG codes. "
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['class-intro-spatial-r']
permalink: /courses/earth-analytics/spatial-data-r/understand-epsg-wkt-and-other-crs-definition-file-types/
nav-title: 'EPSG, Proj4, WKT crs Formats'
week: 4
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 5
topics:
  spatial-data-and-gis: ['vector-data', 'coordinate-reference-systems']
  reproducible-science-and-programming:
---


{% include toc title="In This Lesson" icon="file-text" %}



This lesson discusses ways that coordinate reference system data are stored
including `proj4`, well known text (`wkt`) and `EPSG` codes.

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Identify the `proj4` vs `EPSG` vs `WKT` crs format when presented with all three formats.
* Look up a `CRS` definition in `proj4`, `EPSG` or `WKT` formats using spatialreference.org.
* Create a `proj4` string in `R` using an `EPSG` code.
* Look up an `proj4` string using an `epsg` code with `dplyr` pipes the the `make_EPSG()` function.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data 
for week 4 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 4 Data (~500 MB)](https://ndownloader.figshare.com/files/7525363){:data-proofer-ignore='' .btn }

</div>

In the previous lessons you learned what a coordinate reference system (`CRS`) is, the
components of a coordinate reference system and the general differences between
projected and geographic coordinate reference systems. In this lesson you will
cover the different ways that `CRS` information is stored.

### Coordinate Reference System Formats

There are numerous formats that are used to document a `CRS`. Three common
formats include:

* **proj.4**
* **EPSG**
* Well-known Text (**WKT**)
formats.

Often you have `CRS` information in one format and you need to translate and use it in a tool like `R`.

One of the most powerful websites to look up `CRS` strings is <a href="http://spatialreference.org/" target="_blank">Spatialreference.org</a>.
You can use the search on the site to find an `EPSG` code. Once you find the page
associated with your `CRS` of interest you can then look at all of the various formats
associated with that `CRS`:
<a href="http://spatialreference.org/ref/epsg/4326/" target="_blank">EPSG 4326 - WGS84 geographic</a>

#### PROJ or PROJ.4 Strings

`PROJ.4` strings are a compact way to identify a spatial or coordinate reference
system. `PROJ.4` strings are the primary output from many of the spatial data `R`
packages that you will use (e.g. `raster`, `rgdal`). Note that the `sf` package
is moving towards the more concise `EPSG` format.

Using the `PROJ.4` syntax, you specify the complete set of parameters including
the ellipse, datum, projection units and projection definition that define a particular `CRS`.

The `sp` package in `R`, by default often uses the `proj4` format to define
`CRS` of an object. Let's explore some data to see.


```r
# load packages
library(raster)
library(rgdal)
library(dplyr)
library(stringr)
```



















