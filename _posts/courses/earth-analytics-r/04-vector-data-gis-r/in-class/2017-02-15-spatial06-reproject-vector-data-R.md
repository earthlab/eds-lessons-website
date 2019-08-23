---
layout: single
title: "GIS in R: How to Reproject Vector Data in Different Coordinate Reference Systems (crs) in R"
excerpt: "In this lesson you learn how to reproject a vector dataset using the spTransform() function in R. "
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['class-intro-spatial-r']
permalink: /courses/earth-analytics/spatial-data-r/reproject-vector-data/
nav-title: 'Reproject Vector Data'
week: 4
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 6
topics:
  spatial-data-and-gis: ['vector-data', 'coordinate-reference-systems']
  reproducible-science-and-programming:
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Describe atleast 2 reasons that a data provider may chose to store a dataset in a particular `CRS`.
* Reproject a vector dataset to another `CRS` in `R`.
* Identify the `CRS` of a spatial dataset in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data for week 4 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 4 Data (~500 MB)](https://ndownloader.figshare.com/files/7525363){:data-proofer-ignore='' .btn }

</div>

## Working with Spatial Data from Different Sources

You often need to gather spatial datasets for from different sources and/or data
that cover different spatial `extents`. Spatial data from different sources and
that cover different extents are often in different Coordinate Reference Systems (`CRS`).

Some reasons for data being in different `CRS`s include:

1. The data are stored in a particular `CRS` convention used by the data
provider which might be a federal agency, or a state planning office.
2. The data are stored in a particular `CRS` that is customized to a region.
For instance, many states prefer to use a **State Plane** projection customized
for that state.

<figure>
    <a href="{{ site.url }}/images/courses/earth-analytics/spatial-data/compare-mercator-utm-wgs-projections.jpg">
    <img src="{{ site.url }}/images/courses/earth-analytics/spatial-data/compare-mercator-utm-wgs-projections.jpg" alt="Maps of the United States using data in different projections.">
    </a>

    <figcaption>Maps of the United States using data in different projections.
    Notice the differences in shape associated with each different projection.
    These differences are a direct result of the calculations used to "flatten"
    the data onto a 2-dimensional map. Often data are stored purposefully in a
    particular projection that optimizes the relative shape and size of
    surrounding geographic boundaries (states, counties, countries, etc).
    Source: opennews.org</figcaption>
</figure>


In this tutorial you will learn how to identify and manage spatial data
in different projections. You will learn how to `reproject` the data so that they
are in the same projection to support plotting / mapping. Note that these skills
are also required for any geoprocessing / spatial analysis. Data need to be in
the same `CRS` to ensure accurate results.

You will use the `rgdal` and `raster` libraries in this tutorial.


```r
# load spatial data packages
library(rgdal)
library(raster)
library(rgeos)
options(stringsAsFactors = FALSE)
# set working directory to data folder
# setwd("pathToDirHere")
```

## Import US Boundaries - Census Data

There are many good sources of boundary base layers that you can use to create a
basemap. Some `R` packages even have these base layers built in to support quick
and efficient mapping. In this tutorial, you will use boundary layers for the
United States, provided by the
<a href="https://www.census.gov/geo/maps-data/data/cbf/cbf_state.html" target="_blank" data-proofer-ignore=''> United States Census Bureau.</a>

It is useful to have shapefiles to work with because you can add additional
attributes to them if need be - for project specific mapping.

## Read US Boundary File

You will use the `readOGR()` function to import the
`/usa-boundary-layers/US-State-Boundaries-Census-2014` layer into `R`. This layer
contains the boundaries of all continental states in the U.S. Please note that
these data have been modified and reprojected from the original data downloaded
from the Census website to support the learning goals of this tutorial.
























