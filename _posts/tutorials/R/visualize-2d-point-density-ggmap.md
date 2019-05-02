---
layout: single 
title: 'Computing and plotting 2d spatial point density in R' 
date: 2016-07-07 
authors: [Max Joseph] 
category: [tutorials] 
excerpt: 'This tutorial demonstrates how to compute 2d spatial density and visualize the result using storm event data from NOAA.' 
sidebar: 
nav: 
author_profile: false 
comments: true 
lang: [r]
lib: [ggmap, viridis]
---


It is often useful to quickly compute a measure of point density and show it on a map. 
In this tutorial, we'll demonstrate this using crime data from Houston, Texas 
contained in the ggmap R package. 

## Objectives

- Compute 2d spatial density of points
- Plot the density surface with ggplot2

## Dependencies

- ggplot2
- ggmap

We'll start by loading libraries.
**Note** the ggmap package is no longer used in this lesson to generate a basemap, due changes in the way that maps are served from Google, but the data used in this tutorial are contained in the ggmap package. 


```r
library(ggplot2)
library(ggmap)
## Error in library(ggmap): there is no package called 'ggmap'
```

Then, we can load a built-in crime dataset for Houston, Texas. 


```r
data(crime)
## Warning in data(crime): data set 'crime' not found

# remove any rows with missing data
crime <- crime[complete.cases(crime), ]
## Error in eval(expr, envir, enclos): object 'crime' not found

# look at the structure of the crime data
str(crime)
## Error in str(crime): object 'crime' not found
```

Let's plot the locations of crimes with ggplot2. 


```r
ggplot(crime, aes(x = lon, y = lat)) + 
  geom_point() + 
  coord_equal() + 
  xlab('Longitude') + 
  ylab('Latitude')
## Error in ggplot(crime, aes(x = lon, y = lat)): object 'crime' not found
```

There seems to be a fair bit of overplotting. 
Let's instead plot a density estimate. 
There are many ways to compute densities, and if the mechanics of density estimation are important for your application, it is worth investigating packages that specialize in point pattern analysis (e.g., [spatstat](https://cran.r-project.org/web/packages/spatstat/index.html)). 
If on the other hand, you're lookng for a quick and dirty implementation for the purposes of exploratory data analysis, you can also use ggplot's [`stat_density2d`](http://ggplot2.tidyverse.org/reference/geom_density_2d.html), which uses [`MASS::kde2d`](https://stat.ethz.ch/R-manual/R-devel/library/MASS/html/kde2d.html) on the backend to estimate the density using a bivariate normal kernel.



```r
ggplot(crime, aes(x = lon, y = lat)) + 
  coord_equal() + 
  xlab('Longitude') + 
  ylab('Latitude') + 
  stat_density2d(aes(fill = ..level..), alpha = .5,
                 geom = "polygon", data = crime) + 
  scale_fill_viridis_c() + 
  theme(legend.position = 'none')
## Error in ggplot(crime, aes(x = lon, y = lat)): object 'crime' not found
```

You can pass arguments for `kde2d` through the call to `stat_density2d`. 
In this case, we alter the argument `h`, which is a bandwidth parameter related to the spatial range or smoothness of the density estimate. 



```r
ggplot(crime, aes(x = lon, y = lat)) + 
  coord_equal() + 
  xlab('Longitude') + 
  ylab('Latitude') + 
  stat_density2d(aes(fill = ..level..), alpha = .5,
                 h = .02, n = 300,
                 geom = "polygon", data = crime) + 
  scale_fill_viridis_c() + 
  theme(legend.position = 'none')
## Error in ggplot(crime, aes(x = lon, y = lat)): object 'crime' not found
```

As an alternative, we might consider plotting the raw data points with alpha transparency so that we can see the actual data, not just a model of the data.
We will also set coordinates to use as limits to focus in on downtown Houston. 


```r
ggplot(crime, aes(x = lon, y = lat)) + 
  geom_point(size = 0.1, alpha = 0.05) + 
  coord_equal() + 
  xlab('Longitude') + 
  ylab('Latitude') + 
  coord_cartesian(xlim = c(-95.1, -95.7), 
                  ylim = c(29.5, 30.1))
## Error in ggplot(crime, aes(x = lon, y = lat)): object 'crime' not found
```

