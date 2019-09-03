---
layout: single
title: "How to Replace Raster Cell Values with Values from A Different Raster Data Set in R"
excerpt: "Often data have missing or bad data values that you need to replace. Learn how to replace missing or bad data values in a raster, with values from another raster in the same pixel location using the cover function in R."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['spectral-data-fire-2-r']
permalink: /courses/earth-analytics/multispectral-remote-sensing-modis/replace-raster-cell-values-in-remote-sensing-images-in-r/
nav-title: 'Replace Raster Cell Values'
week: 8
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 3
topics:
  remote-sensing: ['landsat']
  earth-science: ['fire']
  spatial-data-and-gis: ['raster-data']
  find-and-manage-data: ['missing-data-nan']
lang-lib:
  r: []
---


{% include toc title="In This Lesson" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Use the cover function in R to replace missing or bad data values in a raster with values from another raster

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data for week 8 of the course.

{% include /data_subsets/course_earth_analytics/_data-week6-7.md %}

</div>


First, import and stack the "cleaner" better Landsat data.
Convert it to a rasterbrick.



















