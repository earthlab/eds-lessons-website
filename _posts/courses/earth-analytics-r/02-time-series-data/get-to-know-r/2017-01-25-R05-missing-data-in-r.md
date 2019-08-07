---
layout: single
title: "How to Address Missing Values in R"
excerpt: "Missing data in R can be caused by issues in data collection and / or processing and presents challenges in data analysis. Learn how to address missing data values in R."
authors: ['Leah Wasser', 'Data Carpentry']
category: [courses]
class-lesson: ['get-to-know-r']
permalink: /courses/earth-analytics/time-series-data/missing-data-in-r-na/
nav-title: 'Clean Missing Data'
dateCreated: 2016-12-13
modified: '2019-08-07'
week: 2
sidebar:
  nav:
author_profile: false
comments: true
order: 5
course: "earth-analytics"
topics:
  reproducible-science-and-programming: ['RStudio']
  find-and-manage-data: ['missing-data-nan']
redirect_from:
   - "/course-materials/earth-analytics/week-2/missing-data-in-r-na/"
---

{% include toc title="In This Lesson" icon="file-text" %}




This lesson covers how to work with no data values in `R`.

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives
At the end of this activity, you will be able to:

* Understand why it is important to make note of missing data values.
* Be able to define what a `NA` value is in `R` and how it is used in a vector.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You need `R` and `RStudio` to complete this tutorial. Also we recommend that you
have an `earth-analytics` directory set up on your computer with a `/data`
directory within it.

* [How to set up R / RStudio](/courses/earth-analytics/document-your-science/setup-r-rstudio/)
* [Set up your working directory](/courses/earth-analytics/document-your-science/setup-working-directory/)

</div>

## Missing Data - No Data Values

Sometimes, your data are missing values. Imagine a spreadsheet in Microsoft Excel
with cells that are blank. If the cells are blank, you don't know for sure whether
those data weren't collected, or someone forgot to fill them in. To account
for data that are missing (not by mistake) you can put a value in those cells
that represents `no data`.

The `R` programming language uses the value `NA` to represent missing data values.


```r

planets <- c("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus",
             "Neptune", NA)
```

The default setting for most base functions that read data into `R` is to
interpret `NA` as a missing value.

Let's have a closer look at this using the `boulder_precip` data that you've
used in the previous lessons. Please download the data again as there have
been some changes made!


```r
# download file
download.file("https://ndownloader.figshare.com/files/9282364",
              "data/boulder-precip-temp.csv",
              method = "libcurl")
```

Then you can open the data.





















