---
layout: single
title: "How to Remove Borders and Add Legends to Spatial Plots in R. "
excerpt: "In this lesson you review how to remove those pesky borders from a raster plot using base plot in R. We also cover adding legends to your plot outside of the plot extent."
authors: ['Leah Wasser']
modified: '2019-08-23'
category: [courses]
class-lesson: ['how-to-hints-week8']
permalink: /courses/earth-analytics/multispectral-remote-sensing-modis/refine-plots-report/
nav-title: 'Refine RGB Plots'
week: 8
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 2
topics:
  reproducible-science-and-programming:
  data-exploration-and-analysis: ['data-visualization']
  spatial-data-and-gis: ['raster-data']
redirect_from:
  - "/courses/earth-analytics/week-7/refine-plots-report/"
---

{% include toc title="In This Lesson" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Remove borders and refine the size of plots in an output rmarkdown report.
* Adjust the aspect ratio of a plot rendered to a pdf using knitr.
* Customize the location of legends in a plot in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data for week 8 of the course.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 8 Data (~500 MB)](https://ndownloader.figshare.com/files/7677208){:data-proofer-ignore='' .btn }
</div>




In the previous lessons, you opened landsat and MODIS data in R. In this lesson,
you will learn how to refine your plots in R to make your report look nicer and
in turn more professional. First, let's import some data.







































