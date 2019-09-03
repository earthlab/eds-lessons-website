---
layout: single
title: "GIS in R: Plot Spatial Data and Create Custom Legends in R"
excerpt: "In this lesson you break down the steps required to create a custom legend for spatial data in R. You learn about creating unique symbols per category, customizing colors and placing your legend outside of the plot using the xpd argument combined with x,y placement and margin settings."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['hw-custom-maps-r']
permalink: /courses/earth-analytics/spatial-data-r/r-create-custom-legend-with-base-plot/
nav-title: 'Maps with Base Plot'
module-title: 'Create Maps and Custom Legends in R with ggplot and Base Plot'
module-description: 'Learn how to create maps with custom colors and legends in both base R and with ggplot in R.'
module-nav-title: 'Custom Maps in R'
module-type: 'class'
week: 4
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: false
order: 1
class-order: 2
topics:
  spatial-data-and-gis: ['vector-data', 'coordinate-reference-systems', 'maps-in-r']
  reproducible-science-and-programming:
---


{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Add a custom legend to a map in `R`.
* Plot a vector dataset by attributes in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data for week 4 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 4 Data (~500 MB)](https://ndownloader.figshare.com/files/7525363){:data-proofer-ignore='' .btn }

</div>

## Plot Lines by Attribute Value
To plot vector data with the color of each objected determined by it's associated attribute values, the
attribute values must be class = `factor`. A **factor** is similar to a category
- you can group vector objects by a particular category value - for example you
can group all lines of `TYPE=footpath`. However, in `R`, a factor can also have
a determined *order*.

By default, `R` will import spatial object attributes as `factors`.

<i class="fa fa-star"></i> **Data Tip:** If your data attribute values are not
read in as factors, you can convert the categorical
attribute values using `as.factor()`.
{: .notice--success}




```r
# load libraries
library(raster)
library(rgdal)
options(stringsAsFactors = FALSE)
```

Next, import and explore the data.


















































