---
layout: single
title: "Subset & Aggregate Time Series Precipitation Data in R Using mutate(), group_by() and summarise()"
excerpt: "This lesson introduces the mutate() and group_by() dplyr functions - which allow you to aggregate or summarize time series data by a particular field - in this case you will aggregate data by day to get daily precipitation totals for Boulder during the 2013 floods."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['time-series-r']
week: 2
permalink: /courses/earth-analytics/time-series-data/aggregate-time-series-data-r/
nav-title: 'Bonus: Summarize & Filter Data'
sidebar:
  nav:
author_profile: false
comments: true
order: 5
course: "earth-analytics"
topics:
  reproducible-science-and-programming: ['RStudio']
  time-series:
  data-exploration-and-analysis: ['data-visualization']
---

{% include toc title="In This Lesson" icon="file-text" %}



Bonus / Graduate activity. In this lesson, you will plot precipitation data in `R`.
However, these data were collected over several decades and sometimes there are
multiple data points per day. The data are also not cleaned. You will find
heading names that may not be meaningful, and other issues with the data.

This lesson shows you what the plots should look like but does not
provide each and every step that you need to process the data.
You have the skills that you need from the other lessons
covered this week!

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Aggregate data by a day in `R`.
* View names and rename columns in a `data.frame`.

### Things You'll Need To Complete This Lesson

Please be sure you have the most current version of `R` and, preferably,
`RStudio` to write your code.

 **R skill level:** Intermediate - To succeed in this tutorial, you will need to
have basic knowledge for use of the `R` software program.

### R Libraries to Install:

* **ggplot2:** `install.packages("ggplot2")`
* **plotly:** `install.packages("dplyr")`

#### Data download

If you haven't already downloaded this data (from the previous lesson), do so now.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 02 data](https://ndownloader.figshare.com/files/7426738){:data-proofer-ignore='' .btn }

</div>


## Work with Precipitation Data

## R Libraries

To get started, load the `ggplot2` and `dplyr` libraries, set up your working
directory and set `stringsAsFactors` to FALSE using `options()`.







## Import Precipitation Data

You will use the `805333-precip-daily-1948-2013.csv` dataset for this assignment.
in this analysis. This dataset contains the precipitation values collected daily
from the COOP station 050843 in Boulder, CO for 1 January 2003 through 31 December 2013.

Import the data into `R` and then view the data structure.

























