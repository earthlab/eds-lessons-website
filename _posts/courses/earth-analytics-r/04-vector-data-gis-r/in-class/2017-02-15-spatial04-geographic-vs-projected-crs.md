---
layout: single
title: "GIS With R: Projected vs Geographic Coordinate Reference Systems"
excerpt: "Geographic coordinate reference systems are often used to make maps of the world. Projected coordinate reference systems are use to optimize spatial analysis for a region. Learn about WGS84 and UTM Coordinate Reference Systems as used in R."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['class-intro-spatial-r']
permalink: /courses/earth-analytics/spatial-data-r/geographic-vs-projected-coordinate-reference-systems-UTM/
nav-title: 'Geographic vs Projected CRS'
week: 4
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 4
topics:
  spatial-data-and-gis: ['vector-data', 'coordinate-reference-systems']
  reproducible-science-and-programming:
redirect_from:
   - "/course-materials/earth-analytics/week-4/geographic-vs-projected-coordinate-reference-systems-UTM/"
---


{% include toc title="In This Lesson" icon="file-text" %}



This lesson briefly discusses the key differences between projected vs. geographic
coordinate reference systems.

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* List 2-3 fundamental differences between a geographic and a projected CRS.
* Describe the elements of each zone within a Universal Trans Mercator (UTM) CRS and a Geographic (WGS84) CRS.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data for week 4 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 4 Data (~500 MB)](https://ndownloader.figshare.com/files/7525363){:data-proofer-ignore='' .btn }

</div>

## Geographic vs Projected CRS

In the previous tutorial, you explored the basic concept of a coordinate reference
system. During the lesson you looked at two different types of Coordinate Reference Systems:

1. **Geographic coordinate systems:** coordinate systems that span the entire
globe (e.g. latitude / longitude).
2. **Projected coordinate systems:** coordinate systems that are localized to
minimize visual distortion in a particular region (e.g. Robinson, UTM, State Plane)

In this tutorial, you will learn the differences between these `CRS`'s in more
detail.

As you learned in the previous lesson, each `CRS` is optimized to best represent the:

* shape and/or
* scale / distance and/or
* area

of features in a dataset. There is not a single `CRS` that does a great job at
optimizing all three elements: shape, distance AND area. Some CRSs are optimized
for shape, some are optimized for distance and some are optimized for area. Some
`CRS`'s are also optimized for particular regions, for instance the United States,
or Europe.

## Intro to Geographic Coordinate Reference Systems

Geographic coordinate systems (which are often but not always in decimal degree
units) are often optimal when you need to locate places on the Earth. Or when
you need to create global maps. However, latitude and longitude locations are not
located using uniform measurement units. Thus, geographic `CRS`'s are not ideal
for measuring distance. This is why other projected `CRS` have been developed.

<figure>
	<a href="{{ site.url }}/images/courses/earth-analytics/spatial-data/latitude-longitude-globe-ESRI.gif">
	<img src="{{ site.url }}/images/courses/earth-analytics/spatial-data/latitude-longitude-globe-ESRI.gif" alt="Graphic showing lat long as it's placed over the globe by ESRI."></a>
	<figcaption>A geographic coordinate system locates latitude and longitude
	location using angles. Thus the spacing of each line of latitude moving north
	and south is not uniform.
	Source: ESRI
	</figcaption>
</figure>

## The Structure of a Geographic CRS

A geographic `CRS` uses a grid that wraps around the entire globe. This means that
each point on the globe is defined using the SAME coordinate system and the same
units as defined within that particular geographic CRS. Geographic coordinate
reference systems are best for global analysis however it is important to remember
that distance is distorted using a geographic lat / long `CRS`.

The **geographic WGS84 lat/long** `CRS` has an origin - (0,0) - located at the
intersection of the Equator (0° latitude) and Prime Meridian (0° longitude) on
the globe.

Let's remind ourselves what data projects in a geographic `CRS` look like.

```r
library(ggplot2)
library(rgdal)
library(raster)
```












