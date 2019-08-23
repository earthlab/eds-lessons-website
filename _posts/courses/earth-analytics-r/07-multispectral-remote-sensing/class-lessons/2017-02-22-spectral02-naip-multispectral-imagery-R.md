---
layout: single
title: "How to Open and Work with NAIP Multispectral Imagery in R"
excerpt: "In this lesson you learn how to open up a multi-band raster layer or image stored in .tiff format in R. You are introduced to the stack() function in R which can be used to import more than one band into a stack object in R. You also review using plotRGB to plot a multi-band image using RGB, color-infrared to other band combinations."
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['spectral-data-fire-r']
permalink: /courses/earth-analytics/multispectral-remote-sensing-data/naip-imagery-raster-stacks-in-r/
nav-title: 'Open NAIP Imagery in R'
week: 7
sidebar:
  nav:
author_profile: false
comments: true
course: "earth-analytics"
order: 2
topics:
  remote-sensing: ['naip', 'multispectral-remote-sensing']
  reproducible-science-and-programming:
  spatial-data-and-gis: ['raster-data']
lang-lib:
  r: []
redirect_from:
   - "/courses/earth-analytics/week-6/naip-imagery-raster-stacks-in-r/"
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Open an RGB image with 3-4 bands in `R` using `plotRGB()`.
* Export an RGB image as a Geotiff using `writeRaster()`.
* Identify the number of bands stored in a multi-band raster in `R`.
* Plot various band composite in `R` including True Color (RGB), and Color Infrared (CIR).

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data for week 7 of the course.

{% include /data_subsets/course_earth_analytics/_data-week6-7.md %}
</div>

## Multispectral Imagery in R

### Introduction to Multi-Band Raster Data

In the previous weeks, you have worked with raster data derived from lidar remote sensing
instruments. These rasters consisted of one layer or band and contained information
height values derived from lidar data. In this lesson, you will
learn how to work with rasters containing multispectral imagery data stored within
multiple bands (or layers) in `R`.

Previously, you used the `raster()` function to open raster data in `R`. To work
with multi-band rasters in `R`, you need to change how you import and plot
your data in several ways.

* To import multi-band raster data you will use the `stack()` function.
* If your multi-band data are imagery that you wish to composite, you can use
`plotRGB()`, instead of `plot()`, to plot a 3 band raster image.

<figure>
    <a href="{{ site.url }}/images/courses/earth-analytics/raster-data/single-vs-multi-band-raster-data.png">
    <img src="{{ site.url }}/images/courses/earth-analytics/raster-data/single-vs-multi-band-raster-data.png" alt="A raster can contain one or more bands. You can use the
    raster function to import one single band from a single OR multi-band
    raster.">
    </a>
    <figcaption>A raster can contain one or more bands. You can use the
    raster function to import one single band from a single OR multi-band
    raster. Source: Colin Williams, NEON.</figcaption>
</figure>

## What is Multispectral Imagery?

One type of multispectral imagery that is familiar to many of us is a color
image. A color image consists of three bands: red, green, and blue. Each
band represents light reflected from the red, green or blue portions of the
electromagnetic spectrum. The pixel brightness for each band, when composited
creates the colors that you see in an image. These colors are the ones your eyes
can see within the visible portion of the electromagnetic spectrum.

<figure>
    <a href="{{ site.url }}/images/courses/earth-analytics/raster-data/RGB-bands-raster-stack.jpg">
    <img src="{{ site.url }}/images/courses/earth-analytics/raster-data/RGB-bands-raster-stack.jpg" alt="A color image consists of 3 bands - red, green and blue. When
    rendered together in a GIS, or even a tool like Photoshop or any other
    image software, the 3 bands create a color image."></a>
    <figcaption>A color image consists of 3 bands - red, green and blue. When
    rendered together in a GIS, or even a tool like Photoshop or any other
    image software, the 3 bands create a color image.
	Source: Colin Williams, NEON.
    </figcaption>
</figure>

You can plot each band of a multi-band image individually using a grayscale
color gradient. Remember from the videos that you watched in class that the
LIGHTER colors represent a stronger reflection
in that band. DARKER colors represent a weaker reflection.
























































