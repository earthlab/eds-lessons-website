---
layout: single
title: "Use Tidytext to Text Mine Social Media - Twitter Data Using the Twitter API from Rtweet in R"
excerpt: "This lesson provides an example of modularizing code in R. "
authors: ['Leah Wasser','Carson Farmer']
modified: '2019-08-23'
category: [courses]
class-lesson: ['social-media-r']
permalink: /courses/earth-analytics/get-data-using-apis/text-mine-colorado-flood-tweets-science-r/
nav-title: 'Text Mine CO Flood Tweets'
week: 13
course: "earth-analytics"
module-type: 'class'
sidebar:
  nav:
author_profile: false
comments: true
order: 4
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

* Use the `tidytext` package in `R` to filter social media data by date.
* Use the `tidytext` package in `R` to text mine social media data.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson.

[<i class="fa fa-download" aria-hidden="true"></i> Download Week 13 Data (~80 MB)](https://ndownloader.figshare.com/files/10960175){:data-proofer-ignore='' .btn }

</div>

In the previous lesson you learned the basics of preparing social media data for
analysis and using `tidytext` to analyze tweets. In this lesson you will learn to 
use `tidytext` to text mine tweets and filter them by date. 

The structure of twitter data is complex. In this lesson you will only work with 
the text data of tweets even though there is much more information that you could 
analyze.


```r
# json support
library(rjson)
library(jsonlite)

# plotting and pipes - tidyverse!
library(ggplot2)
library(dplyr)
library(tidyr)
# text mining library
library(tidytext)
library(tm)
# coupled words analysis
library(widyr)
# plotting packages
library(igraph)
library(ggraph)

options(stringsAsFactors = FALSE)
```





























