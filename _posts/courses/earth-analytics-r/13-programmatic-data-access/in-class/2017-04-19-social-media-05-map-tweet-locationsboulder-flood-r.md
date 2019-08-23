---
layout: single
title: "Create Maps of Social Media Twitter Tweet Locations Over Time in R"
excerpt: "This lesson provides an example of modularizing code in R. "
authors: ['Leah Wasser','Carson Farmer']
modified: '2019-08-23'
category: [courses]
class-lesson: ['social-media-r']
permalink: /courses/earth-analytics/get-data-using-apis/map-tweet-locations-over-time-r/
nav-title: 'Map Tweet Locations'
week: 13
course: "earth-analytics"
module-type: 'class'
sidebar:
  nav:
author_profile: false
comments: true
order: 5
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

* Use `ggplot` in `R` to create a static map of social media activity.
* Use leaflet to create an interactive map of social media activity.
* Use `GGAnimate` to create an antimated gif file of social media activity.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson.

</div>


In the previous lesson, you used text mining approaches to understand what people
were tweeting about during the flood. Here, you will create a map that shows the
location from where people were tweeting during the flood.

Keep in mind that these data have already been filtered to only include tweets that
at the time of the flood event, had an x, y location associated with them.
Thus this map doesn't represent all of the tweets that may be related to the flood
event.

You need three packages to create your map:

1. ggplot: You will use `ggplot()` to create your map.
2. You will use the `maps` package to automatically access a basemap containing
boundaries of countries across the globe.
3. Finally you use the `ggthemes` library which includes `theme_map()`. This theme 
turns off all of the extra `ggplot` elements that you don't need such as the x and y axis.



```r
# load twitter library - the rtweet library is recommended now over twitteR
library(rjson)
library(jsonlite)
# plotting and pipes - tidyverse!
library(ggplot2)
library(dplyr)
library(tidyr)

# animated maps
# to install: devtools::install_github("dgrtwo/gganimate")
# note this required imagemagick to be installed
library(leaflet)
library(gganimate)
library(lubridate)
library(maps)
library(ggthemes)

options(stringsAsFactors = FALSE)
```



























