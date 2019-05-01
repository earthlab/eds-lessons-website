---
layout: single 
title: "Visualizing hourly traffic crime data for Denver, Colorado using R, dplyr, and ggplot"
date: 2016-12-06 
authors: [Max Joseph] 
category: [tutorials] 
excerpt: 'This tutorial demonstrates how to access and visualize crime data for Denver, Colorado.' 
sidebar: 
nav: 
author_profile: false 
comments: true 
lang: [r]
lib: [dplyr, ggplot2, lubridate, viridis, RCurl]
---
# test

The city of Denver publicly hosts crime data from the past five years in their open data catalog.
In this tutorial, we will use R to access and visualize these data, which are essentially spatiotemporally referenced points with features for type of crime, neighborhood, etc. 

First, we will load some packages that we'll use later. 


```r
library(dplyr)
library(ggplot2)
library(lubridate)
## Error in library(lubridate): there is no package called 'lubridate'
library(viridis)
## Error in library(viridis): there is no package called 'viridis'
library(RCurl)
## Error in library(RCurl): there is no package called 'RCurl'
```

Then, we need to download a comma separated values file that contains the raw data.


```r
data_url <- "http://data.denvergov.org/download/gis/crime/csv/crime.csv"
data <- getURL(data_url, ssl.verifypeer = 0L, followlocation = 1L)
## Error in eval(expr, envir, enclos): could not find function "getURL"
d <- read.csv(text = data)
## Error in textConnection(text, encoding = "UTF-8"): invalid 'text' argument
```

Let's lowercase the column names, and look at the structure of the data with the `str()` function. 


```r
names(d) <- tolower(names(d))
## Error in tolower(names(d)): object 'd' not found
str(d)
## Error in str(d): object 'd' not found
```

The code below uses the `dplyr` package to subset the data to only include traffic accident crimes (`filter(...)`), and parses the date/time column so that we can extract quantities like hour-minutes (to evaluate patterns over the course of one day), the day of week (e.g., 1 = Sunday, 2 = Monday, ...), and year day (what day of the year is it?), creating new columns for these variables with the `mutate()` function.


```r
accidents <- d %>%
  filter(offense_category_id == "traffic-accident") %>%
  mutate(datetime = ymd_hms(first_occurrence_date, tz = "MST"),
         hm = as.POSIXct(paste(hour(datetime), minute(datetime), sep = ":"), 
                         format = "%H:%M"),
         dow = wday(datetime), 
         yday = yday(datetime))
## Error in eval(expr, envir, enclos): object 'd' not found
```

Last, we will group our data by hour-minute and day of the week, and for each combination of these two quantities, compute the number of traffic accident crimes. 
Then we'll create a new variable `day`, which is the character representation (Sunday, Monday, ...) of the numeric `dow` column (1, 2, ...).
We'll also create a new variable `offense_type`, which is a more human-readable version of the `offense-type-id` column.
Using ggplot, we'll create a density plot with a color for each day of week.
This workflow uses `dplyr` to munge our data, then pipes the result to `ggplot2`, so that we only create one object in our global environment `p`, which is our plot. 


```r
p <- accidents %>%
  group_by(hm, dow, yday, offense_type_id) %>%
  summarize(n = n()) %>%
  # the call to mutate() makes new variables with better names
  mutate(day = factor(c("Sunday", "Monday", "Tuesday", 
                 "Wednesday", "Thursday", "Friday", 
                 "Saturday")[dow], 
                 levels = c("Monday", "Tuesday", 
                            "Wednesday", "Thursday", "Friday", 
                            "Saturday", "Sunday")), 
         offense_type = ifelse(
           offense_type_id == "traffic-accident-hit-and-run", 
           "Hit and run", 
           ifelse(
             offense_type_id == "traffic-accident-dui-duid",
             "Driving under the influence", "Traffic accident"))) %>%
  ggplot(aes(x = hm, 
             fill = day, 
             color = day)) + 
  geom_freqpoly(binwidth = 60 * 30) + # 60 sec/min * 30 min
  scale_color_viridis(discrete = TRUE, "", direction = -1) + 
  scale_fill_viridis(discrete = TRUE, "", direction = -1) + 
  xlab("Time of day") + 
  ylab("Frequency") + 
  ggtitle("Traffic crimes in Denver, Colorado") + 
  scale_x_datetime(date_breaks = "4 hours", date_labels = "%H:%M")
## Error in eval(expr, envir, enclos): object 'accidents' not found
p 
## Error in eval(expr, envir, enclos): object 'p' not found
```

This dplyr to ggplot approach is extremely modular. 
If we wanted to see this plot for each type of traffic accident crime, we could do so simply by adding one statement. 


```r
p + facet_wrap(~ offense_type, ncol = 1, scales = "free_y")
## Error in eval(expr, envir, enclos): object 'p' not found
```
