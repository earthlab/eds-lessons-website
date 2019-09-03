---
layout: single
title: "Summarize Time Series Data by Month or Year Using Tidyverse Pipes in R"
excerpt: "Learn how to summarize time series data by day, month or year with Tidyverse pipes in R."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['time-series-r']
permalink: /courses/earth-analytics/time-series-data/summarize-time-series-by-month-in-r/
nav-title: 'Summarize Time Series Data'
week: 2
sidebar:
  nav:
author_profile: false
comments: true
order: 3
course: "earth-analytics"
topics:
  reproducible-science-and-programming: ['RStudio']
  time-series:
  data-exploration-and-analysis: ['data-visualization']
---

{% include toc title="In This Lesson" icon="file-text" %}



In this lesson, you will learn about time series data by various time units
including month, day and year.

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Summarize time series data by a particular time unit (e.g. month to year, day to month, using pipes etc.).
* Use `dplyr` pipes to manipulate data in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You need `R` and `RStudio` to complete this tutorial. Also you should have
an `earth-analytics` directory set up on your computer with a `/data`
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


## Get Started with Time Series Data
To begin, load the `ggplot2` and `dplyr` libraries. Also, set your
working directory. Finally, set `stringsAsFactors` to `FALSE` globally using
`options(stringsAsFactors = FALSE)`.




```r
# set your working directory to the earth-analytics directory
# setwd("working-dir-path-here")

# load packages
library(ggplot2)
library(dplyr)
library(lubridate)

# set strings as factors to false
options(stringsAsFactors = FALSE)
```

## Import Precipitation Time Series Data

You will use the same precipitation data that you used in the last lesson. The
data cover the time span between 1 January 2003 through 31 December 2013.
You have a single data point for each day in this dataset. However you are interested
in summary values per MONTH instead of per day.

To begin, use `read.csv()` to import the `.csv` file as you did in the last lesson.
































