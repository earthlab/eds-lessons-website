---
layout: single
title: "An Example of Creating Modular Code in R - Efficient Scientific Programming"
excerpt: "This lesson provides an example of modularizing code in R. "
authors: ['Carson Farmer', 'Leah Wasser', 'Max Joseph']
modified: '2019-09-03'
category: [courses]
class-lesson: ['intro-APIs-r']
permalink: /courses/earth-analytics/get-data-using-apis/get-data-with-rcurl-r/
nav-title: 'Intro to RCurl'
week: 13
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 2
topics:
  find-and-manage-data: ['apis']
redirect_from:
   - "/courses/earth-analytics/week-10/get-data-with-rcurl-r/"
---

{% include toc title = "In This Lesson" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Access data from a remote URL (http or https) using `read.table()` function.
* Explain the difference between accessing data using `download.file()` compared to `read.table()` or `read.csv()`.
* Plot tabular data using `ggplot()`.
* Create a plot with data subsetted by a particular variable using facets.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data that you already downloaded for week 13 of the course.

</div>





```r
library(dplyr)
library(ggplot2)
library(RCurl)
```

## Direct Data Access

In this lesson, you will learn how to access data via a direct download in `R`.
You downloaded data in the first week of this class using `download.file()`
When you used `download.file()`, you were literally downloading that file,
which happened to be in `.csv` (comma separated value) text format to your computer.

You specified the location where that file would download to, using the `destfile=`
argument. Notice below, I specified week 13 as the download location given
that is your current class week.


```r
# download text file to a specified location on your computer
download.file(url = "https://ndownloader.figshare.com/files/7010681",
              destfile = "data/week-13/boulder-precip-aug-oct-2013.csv")
```


If `R` is able to communicate with the server (in this case Figshare) and download
the file, you can then open up the file and plot the data within it.


















