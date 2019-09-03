---
layout: single
title: "Classify a Raster in R."
excerpt: "This lesson presents how to classify a raster dataset and export it as a
new raster in R."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['intro-lidar-raster-r']
permalink: /courses/earth-analytics/lidar-raster-data-r/classify-raster/
nav-title: 'Classify a Raster'
week: 3
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 5
topics:
  reproducible-science-and-programming:
  remote-sensing: ['lidar']
  earth-science: ['vegetation']
  spatial-data-and-gis: ['raster-data']
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Reclassify a raster dataset in `R` using a set of defined values.
* Describe the difference between using breaks to plot a raster compared to
reclassifying a raster object.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You need `R` and `RStudio` to complete this tutorial. Also you should have
an `earth-analytics` directory set up on your computer with a `/data`
directory with it.

* [How to set up R / RStudio](/courses/earth-analytics/document-your-science/setup-r-rstudio/)
* [Set up your working directory](/courses/earth-analytics/document-your-science/setup-working-directory/)
* [Intro to the R & RStudio interface](/courses/earth-analytics/document-your-science/intro-to-r-and-rstudio)

### R Libraries to Install:

* **raster:** `install.packages("raster")`
* **rgdal:** `install.packages("rgdal")`

If you have not already downloaded the week 3 data, please do so now.
[<i class="fa fa-download" aria-hidden="true"></i> Download Week 3 Data (~250 MB)](https://ndownloader.figshare.com/files/7446715){:data-proofer-ignore='' .btn }

</div>

### Reclassification vs. Breaks

In this lesson, you will learn how to reclassify a raster dataset in `R`. Previously,
you plotted a raster value using break points - that is to say, you colored particular
ranges of raster pixels using a defined set of values that you call `breaks`.
In this lesson, you will learn how to reclassify a raster. When you reclassify
a raster you create a **new** raster object / file that can be exported and shared
with colleagues and / or opened in other tools such as `QGIS`.


<figure>
<img src="http://resources.esri.com/help/9.3/arcgisdesktop/com/gp_toolref/geoprocessing_with_3d_analyst/Reclass_Reclass2.gif" alt="reclassification process by ESRI">
<figcaption>When you reclassify a raster you create a new raster. In that raster, each cell from the old raster is mapped to the new raster. The values in the new raster are applied using a defined range of values or a raster map. For example above you can see that all cells that
contain the values 1-3 are assigned the new value of 5. Image source: ESRI.
</figcaption>
</figure>

## Load Libraries




```r
# load the raster and rgdal libraries
library(raster)
library(rgdal)
```

## Raster Classification Steps

You can break your raster processing workflow into several steps as follows:

* **Data import / cleanup:** Load and "clean" the data. This may include cropping, dealing with `NA` values, etc.
* **Data exploration:** Understand the range and distribution of values in your data. This may involve plotting histograms scatter plots, etc.
* **More data processing & analysis:** This may include the final data processing steps that you determined based upon the data exploration phase.
* **Final data analysis:** The final steps of your analysis - often performed using information gathered in the early data processing / exploration stages of your workflow.
* **Presentation:** Refining your results into a final plot or set of plots that are cleaned up, labeled, etc.

Please note - working with data is not a linear process. There are no defined
steps. As you work with data more, you will develop your own workflow and approach.

To get started, let's first open up your raster. In this case you are using the lidar
canopy height model (`CHM`) that you calculated in the previous lesson.





































