---
layout: single
title: "Use Tidyverse Pipes to Subset Time Series Data in R"
excerpt: "Learn how to extract and plot data by a range of dates using pipes in R."
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['time-series-r']
permalink: /courses/earth-analytics/time-series-data/subset-time-series-data-in-r/
nav-title: 'Subset Time Series Data'
week: 2
sidebar:
  nav:
author_profile: false
comments: true
order: 2
course: "earth-analytics"
topics:
  reproducible-science-and-programming: ['RStudio']
  time-series:
  data-exploration-and-analysis: ['data-visualization']
---

{% include toc title="In This Lesson" icon="file-text" %}





In this lesson, you will learn how to import a larger dataset, and test your
skills cleaning and plotting the data.


<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Subset data using the dplyr `filter()` function.
* Use `dplyr` pipes to manipulate data in `R`.
* Describe what a pipe does and how it is used to manipulate data in `R`

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You need `R` and `RStudio` to complete this tutorial. Also we recommend that you
have an `earth-analytics` directory set up on your computer with a `/data`
directory within it.

* [How to set up R / RStudio](/courses/earth-analytics/document-your-science/setup-r-rstudio/)
* [Set up your working directory](/courses/earth-analytics/document-your-science/setup-working-directory/)
* [Intro to the R & RStudio Interface](/courses/earth-analytics/document-your-science/intro-to-r-and-rstudio)

### R Libraries to Install:

* **ggplot2:** `install.packages("ggplot2")`
* **dplyr:** `install.packages("dplyr")`
* **lubridate:** `install.packages("lubridate")`

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 2 Data](https://ndownloader.figshare.com/files/7426738){:data-proofer-ignore='' .btn }

</div>

## Important - Data Organization
Before you begin this lesson, be sure that you've downloaded the dataset above.
You will need to UNZIP the zip file. When you do this, be sure that your directory
looks like the image below: note that all of the data are within the week2
directory. They are not nested within another directory. You may have to copy and
paste your files to make this look right.

<figure>
<a href="{{ site.url }}/images/courses/earth-analytics/co-flood-lessons/week-02-data.png">
<img src="{{ site.url }}/images/courses/earth-analytics/co-flood-lessons/week-02-data.png" alt="week 2 file organization">
</a>
<figcaption>Your `week_02` file directory should look like the one above. Note that
the data directory is directly under the earth-analytics folder.</figcaption>
</figure>

## Get Started with Time Series Data
To begin, load the `ggplot2` and `dplyr` libraries. Also, set your
working directory. Finally, set `stringsAsFactors` to `FALSE` globally using
`options(stringsAsFactors = FALSE)`.


```r
# set your working directory to the earth-analytics directory
# setwd("working-dir-path-here")

# load packages
library(ggplot2)
library(lubridate)
library(dplyr)

# set strings as factors to false
options(stringsAsFactors = FALSE)
```

## Import Precipitation Time Series

You will use a precipitation dataset collected by the
National Centers for Environmental Information (formerly
National Climate Data Center) Cooperative Observer Network (COOP)
station 050843 in Boulder, CO. The data cover the time span between 1 January
2003 through 31 December 2013.

To begin, use `read.csv()` to import the `.csv` file.


































