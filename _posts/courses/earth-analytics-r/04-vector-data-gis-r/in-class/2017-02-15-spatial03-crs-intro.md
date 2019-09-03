---
layout: single
title: "Coordinate Reference System and Spatial Projection"
excerpt: "Coordinate reference systems are used to convert locations on the earth which is round, to a two dimensional (flat) map. Learn about the differences between coordinate reference systems."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['class-intro-spatial-r']
permalink: /courses/earth-analytics/spatial-data-r/intro-to-coordinate-reference-systems/
nav-title: 'Coordinate Reference Systems'
week: 4
sidebar:
  nav:
author_profile: false
comments: true
order: 3
course: "earth-analytics"
topics:
  spatial-data-and-gis: ['vector-data', 'coordinate-reference-systems']
  reproducible-science-and-programming:
redirect_from:
   - "/course-materials/earth-analytics/week-4/intro-to-coordinate-reference-systems/"
---

{% include toc title="In This Lesson" icon="file-text" %}



This lesson covers the key spatial attributes that are needed to work with
spatial data including: Coordinate Reference Systems (`CRS`), extent and spatial resolution.

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Describe what a Coordinate Reference System (`CRS`) is
* List the steps associated with plotting 2 datasets stored using different coordinate reference systems

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data for week 4 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 4 Data (~500 MB)](https://ndownloader.figshare.com/files/7525363){:data-proofer-ignore='' .btn }

</div>

## Intro to Coordinate Reference Systems

In summary - a coordinate reference system (`CRS`) refers to the way in which
spatial data that represent the earth's surface (which is round / 3 dimensional)
are flattened so that you can "Draw" them on a 2-dimensional surface. However each
using a different (sometimes) mathematical approach to performing the flattening
resulting in different coordinate system grids (discussed below). These approaches
to flattening the data are specifically designed to optimize the accuracy of the
data in terms of length and area (more on that later too).

In this lesson you will explore what a `CRS` is. And how it can impact your data
when you are working with it in a tool like `R` (or any other tool).

***

<figure>
    <a href="{{ site.url }}/images/courses/earth-analytics/spatial-data/compare-mercator-utm-wgs-projections.jpg">
    <img src="{{ site.url }}/images/courses/earth-analytics/spatial-data/compare-mercator-utm-wgs-projections.jpg" alt="Maps of the United States in different CRS including Mercator
    (upper left), Albers equal area (lower left), UTM (Upper RIGHT) and
    WGS84 Geographic (Lower RIGHT).">
    </a>

    <figcaption>Maps of the United States in different CRS including Mercator
    (upper left), Albers equal area (lower left), UTM (Upper RIGHT) and
    WGS84 Geographic (Lower RIGHT).
    Notice the differences in shape and orientation associated with each
    CRS. These differences are a direct result of the
    calculations used to "flatten" the data onto a two dimensional map.
    Source: opennews.org</figcaption>
</figure>


<figure>
    <a href="{{ site.url }}/images/courses/earth-analytics/spatial-data/human-head-projections.jpg">
    <img src="{{ site.url }}/images/courses/earth-analytics/spatial-data/human-head-projections.jpg" alt="The human head projected using different coordinate reference systems. SOURCE: Scientific American.">
    </a>

    <figcaption>The human head projected using different coordinate reference systems. SOURCE: Scientific American. Do any of these happen to bare a striking resemblance to Jay Leno? </figcaption>
</figure>

The short video below highlights how map projections can make continents
look proportionally larger or smaller than they actually are.

<iframe width="560" height="315" src="https://www.youtube.com/embed/KUF_Ckv8HbE" frameborder="0" allowfullscreen></iframe>

## What is a Coordinate Reference System

To define the location of something you often use a coordinate system. This system
consists of an X and a Y value located within a 2 (or more) -dimensional space.

<figure>
	<a href="{{ site.url}}/images/courses/earth-analytics/spatial-data/coordinate-system.png">
	<img src="{{ site.url}}/images/courses/earth-analytics/spatial-data/coordinate-system.png" alt="You use coordinate systems with X, Y (and sometimes Z axes) to	define the location of objects in space."></a>
	<figcaption> You use coordinate systems with X, Y (and sometimes Z axes) to
	define the location of objects in space.
	Source: http://open.senecac.on.ca
	</figcaption>
</figure>

While the above coordinate system is 2-dimensional, we live on a 3-dimensional
earth that happens to be "round". To define the location of objects on the Earth,
which is round, you need a coordinate system that adapts to the Earth's shape.
When you make maps on paper or on a flat computer screen, you move from a 3-Dimensional
space (the globe) to a 2-Dimensional space (your computer screens or a piece of paper).
The components of the `CRS` define how the "flattening" of data that exists in a 3-D
globe space. The `CRS` also defines the the coordinate system itself.

<figure>
	<a href="{{ site.url}}/images/courses/earth-analytics/spatial-data/geographic-origin.png">
	<img src="{{ site.url}}/images/courses/earth-analytics/spatial-data/geographic-origin.png" alt="A CRS defines the translation between a location on the round earth	and that same location, on a flattened, 2 dimensional coordinate system."></a>
	<figcaption>A CRS defines the translation between a location on the round earth
	and that same location, on a flattened, 2 dimensional coordinate system.
	Source: http://ayresriverblog.com
	</figcaption>
</figure>

> A coordinate reference system (CRS) is a
coordinate-based local, regional or global system used to locate geographical
entities. -- Wikipedia

## The Components of a CRS

The coordinate reference system is made up of several key components:

* **Coordinate system:** The X, Y grid upon which your data is overlayed and how
you define where a point is located in space.
* **Horizontal and vertical units:** The units used to define the grid along the
x, y (and z) axis.
* **Datum:** A modeled version of the shape of the Earth which defines the origin
used to place the coordinate system in space. You will learn this further below.
* **Projection Information:** The mathematical equation used to flatten objects
that are on a round surface (e.g. the Earth) so you can view them on a flat surface
(e.g. your computer screens or a paper map).

## Why CRS is Important

It is important to understand the coordinate system that your data uses -
particularly if you are working with different data stored in different coordinate
systems. If you have data from the same location that are stored in different
coordinate reference systems, **they will not line up in any GIS or other program**
unless you have a program like `ArcGIS` or `QGIS` that supports **projection on the
fly**. Even if you work in a tool that supports projection on the fly, you will
want to all of your data in the same projection for performing analysis and processing
tasks.

<i class="fa fa-star"></i> **Data Tip:** <a href="http://spatialreference.org/ref/epsg/" target="_blank"> spatialreference.org </a>provides an excellent online library of CRS information.
{: .notice--success}

### Coordinate System & Units

You can define a spatial location, such as a plot location, using an x- and a
y-value - similar to your cartesian coordinate system displayed in the figure,
above.

For example, the map below, generated in `R` with `ggplot2` shows all of the
continents in the world, in a `Geographic` Coordinate Reference System. The
units are degrees and the coordinate system itself is **latitude** and
**longitude** with the `origin` being the location where the equator meets
the central meridian on the globe (0,0).



```r
# devtools::install_github("tidyverse/ggplot2")
# load libraries
library(rgdal)
library(ggplot2)
library(rgeos)
library(raster)

#install.packages('sf')
# testing the sf package out for these lessons!
library(sf)
# set your working directory
# setwd("~/Documents/earth-analytics/")
```

In the plot below, you will be using the following theme. You can copy and paste
this code if you'd like to use the same theme!


```r
# turn off axis elements in ggplot for better visual comparison
newTheme <- list(theme(line = element_blank(),
      axis.text.x = element_blank(),
      axis.text.y = element_blank(),
      axis.ticks = element_blank(), # turn off ticks
      axis.title.x = element_blank(), # turn off titles
      axis.title.y = element_blank(),
      legend.position = "none")) # turn off legend
```
































