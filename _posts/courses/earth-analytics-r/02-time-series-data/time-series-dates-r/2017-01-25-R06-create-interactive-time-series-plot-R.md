---
layout: single
title: "Create Interactive Plots in R - Time Series & Scatterplots Using plotly and dygraphs"
excerpt: "Learn how to create interactive reports using plotly and dygraphs in R for plotting. "
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['time-series-r']
permalink: /courses/earth-analytics/time-series-data/interactive-time-series-plots-in-r/
nav-title: 'Interactive Time Series Plots'
week: 2
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 6
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Create an interactive time series plot using `plot.ly` in `R`.
* Create an interactive time series plot using `dygraphs` in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the data for week 4 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 4 Data (~500 MB)](https://ndownloader.figshare.com/files/7525363){:data-proofer-ignore='' .btn }

</div>



In this lesson you will explore using 2 interactive tools to create interactive
plots of your data:

1. `plotly`
2. `dygraphs`

First, you will load all of the needed libraries.


```r
# install plotly from git - ropensci
#devtools::install_github('ropensci/plotly')

# load libraries
library(ggplot2)
library(xts)
library(dygraphs)
library(plotly)

options(stringsAsFactors = FALSE)
```



Next, let's import some time series data



















