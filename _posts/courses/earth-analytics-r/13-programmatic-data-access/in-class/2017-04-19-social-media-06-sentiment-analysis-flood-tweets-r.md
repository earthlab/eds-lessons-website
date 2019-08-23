---
layout: single
title: "Sentiment Analysis of Colorado Flood Tweets in R"
excerpt: "Learn how to perform a basic sentiment analysis using the tidytext package in R. "
authors: ['Leah Wasser','Carson Farmer']
modified: '2019-08-23'
category: [courses]
class-lesson: ['social-media-r']
permalink: /courses/earth-analytics/get-data-using-apis/sentiment-analysis-of-twitter-data-r/
nav-title: 'Sentiment Analysis'
week: 13
course: "earth-analytics"
module-type: 'class'
sidebar:
  nav:
author_profile: false
comments: true
order: 6
lang-lib:
  r: ['rtweet', 'tidytext', 'dplyr']
topics:
  social-science: ['social-media']
  data-exploration-and-analysis: ['text-mining']
---



{% include toc title = "In This Lesson" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Use the `tidytext` package in `R` to perform a sentiment analysis of tweets.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson.

</div>

In the previous lessons you learned to use text mining approaches to understand what 
people are tweeting about and create maps of tweet locations. This lesson will take
that analysis a step further by performing a sentiment analysis of tweets.


```r
# json libraries
library(rjson)
library(jsonlite)
# plotting and pipes - tidyverse!
library(ggplot2)
library(dplyr)
library(tidyr)
library(tidytext)
# date time
library(lubridate)
library(zoo)

options(stringsAsFactors = FALSE)
```











