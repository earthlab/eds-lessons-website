---
layout: single
title: "Homework Challenge: Plot USGS Stream Discharge Data in R"
excerpt: "This lesson illustrated what your final stream discharge homework
plots should look like for the week. Use all of the skills that you've learned in the previous lessons to complete it."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['time-series-r']
week: 2
permalink: /courses/earth-analytics/time-series-data/plot-stream-discharge-timeseries-challenge-r/
nav-title: 'Homework example: Stream Discharge'
sidebar:
  nav:
author_profile: false
comments: true
order: 4
course: "earth-analytics"
topics:
  reproducible-science-and-programming: ['RStudio']
  time-series:
  data-exploration-and-analysis: ['data-visualization']
---


{% include toc title="In This Lesson" icon="file-text" %}



In this data lesson, you explore and visualize stream discharge time series
data collected by the United States Geological Survey (USGS). You will use everything
that you learned in the previous lessons to create your plots. You will use these
plots in the report that you submit for your homework.

Note: this page just shows you what the plots should look like. You will need
to use your programming skills to create the plots!

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Plot USGS Stream Discharge time series data in `R`

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You need `R` and `RStudio` to complete this tutorial. Also you should have
an `earth-analytics` directory set up on your computer with a `/data`
directory with it.

* [How to set up R / RStudio](/courses/earth-analytics/document-your-science/setup-r-rstudio/)
* [Set up your working directory](/courses/earth-analytics/document-your-science/setup-working-directory/)
* [Intro to the R & RStudio Interface](/courses/earth-analytics/document-your-science/intro-to-r-and-rstudio)

### R Libraries to Install:

* **ggplot2:** `install.packages("ggplot2")`
* **dplyr:** `install.packages("dplyr")`

If you haven't already downloaded this data (from the previous lesson), do so now.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 2 Data](https://ndownloader.figshare.com/files/7426738){:data-proofer-ignore='' .btn }

</div>

## About the Data - USGS Stream Discharge Data

The USGS has a distributed network of aquatic sensors located in streams across
the United States. This network monitors a suit of variables that are important
to stream morphology and health. One of the metrics that this sensor network
monitors is **Stream Discharge**, a metric which quantifies the volume of water
moving down a stream. Discharge is an ideal metric to quantify flow, which
increases significantly during a flood event.

> As defined by USGS: Discharge is the volume of water moving down a stream or
> river per unit of time, commonly expressed in cubic feet per second or gallons
> per day. In general, river discharge is computed by multiplying the area of
> water in a channel cross section by the average velocity of the water in that
> cross section.
>
> <a href="http://water.usgs.gov/edu/streamflow2.html" target="_blank">
Read more about stream discharge data collected by USGS.</a>

<figure>
<a href="{{ site.url }}/images/courses/earth-analytics/co-flood-lessons/USGS-peak-discharge.gif">
<img src="{{ site.url }}/images/courses/earth-analytics/co-flood-lessons/USGS-peak-discharge.gif" alt="Plot of stream discharge from the USGS boulder creek stream gage"></a>
<figcaption>
The USGS tracks stream discharge through time at locations across the United
States. Note the pattern observed in the plot above. The peak recorded discharge
value in 2013 was significantly larger than what was observed in other years.
Source: <a href="http://nwis.waterdata.usgs.gov/usa/nwis/peak/?site_no=06730200" target="_blank"> USGS, National Water Information System. </a>
</figcaption>
</figure>

As you can imagine, stream gages can be sensitive to high flows and in the case of
an extreme event like a flood are sometimes damaged. However, during the 2013 floods,
one stream gage in Boulder, Colorado remained in tact. USGS stream gauge 06730200
located on Boulder Creek at North 75th St. collected data that you will use in
the lesson below!




## Work with USGS Stream Gage Data

Let's begin by loading your libraries and setting your working directory.


```r
# set your working directory
# setwd("working-dir-path-here")

# load packages
library(ggplot2) # create efficient, professional plots
library(dplyr) # data manipulation

# set strings as factors to false
options(stringsAsFactors = FALSE)
```

##  Import USGS Stream Discharge Data into R

Let's first import your data using the `read.csv()` function.












