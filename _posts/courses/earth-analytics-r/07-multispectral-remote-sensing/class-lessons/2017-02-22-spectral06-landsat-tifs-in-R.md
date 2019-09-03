---
layout: single
title: "Landsat Remote Sensing tif Files in R"
excerpt: "In this lesson you will cover the basics of using Landsat 7 and 8 in R. You will learn how to import Landsat data stored in .tif format - where each .tif file represents a single band rather than a stack of bands. Finally you will plot the data using various 3 band combinations including RGB and color-infrared."
authors: ['Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['spectral-data-fire-r']
permalink: /courses/earth-analytics/multispectral-remote-sensing-data/landsat-data-in-r-geotiff/
nav-title: 'Landsat tifs in R'
week: 7
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
order: 6
topics:
  remote-sensing: ['landsat']
  earth-science: ['fire']
  reproducible-science-and-programming:
  spatial-data-and-gis: ['raster-data']
lang-lib:
  r: []
redirect_from:
   - "/courses/earth-analytics/week-6/landsat-bands-geotif-in-R/"
   - "/courses/earth-analytics/spectral-remote-sensing-landsat/landsat-bands-geotif-in-R/"

---


{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Use `list.files()` to create a subsetted list of file names within a specified directory on your computer.
* Create a raster stack from a list of `.tif` files in `R`.
* Plot various band combinations using a rasterstack in `R` with `plotRGB()`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
data for week 7 of the course.

{% include /data_subsets/course_earth_analytics/_data-week6-7.md %}

</div>

In the previous lesson, you learned how to import a multi-band image into `R` using
the `stack()` function. You then plotted the data as a composite, RGB (and CIR) image
using `plotRGB()`. However, sometimes data are downloaded in individual bands rather
than a composite raster stack.

In this lesson you will learn how to work with Landsat data in `R`. In this case, your
data are downloaded in `.tif` format with each `.tif` file representing a single
band rather than a stack of bands.

## About Landsat Data

> At over 40 years, the Landsat series of satellites provides the longest temporal record of moderate resolution multispectral data of the Earth’s surface on a global basis. The Landsat record has remained remarkably unbroken, proving a unique resource to assist a broad range of specialists in managing the world’s food, water, forests, and other natural resources for a growing world population.  It is a record unmatched in quality, detail, coverage, and value. Source: <a href="https://landsat.usgs.gov/about-landsat" target="_blank">USGS</a>



<figure>
    <a href="{{ site.url }}/images/courses/earth-analytics/remote-sensing/TimelineOnlyForWebRGB.png">
    <img src="{{ site.url }}/images/courses/earth-analytics/remote-sensing/TimelineOnlyForWebRGB.png" alt="Landsat 40 year timeline source: USGS.">
    </a>
    <figcaption>The 40 year history of Landsat missions. Source: USGS - <a href="https://landsat.usgs.gov/landsat-missions-timeline" target = "_blank"> USGS Landsat</a>
    </figcaption>
</figure>

Landsat data is a multispectral dataset collected from space. The multispectral bands
and associated spatial resolution of the first 9 bands in the Landsat 8 sensor
are listed below.

#### Landsat 8 Bands

| Band | Wavelength range (nanometers) | Spatial Resolution (m) | Spectral Width (nm)|
|-------------------------------------|------------------|--------------------|----------------|
| Band 1 - Coastal aerosol | 430 - 450 | 30 | 2.0 |
| Band 2 - Blue | 450 - 510 | 30 | 6.0 |
| Band 3 - Green | 530 - 590 | 30 | 6.0 |
| Band 4 - Red | 640 - 670 | 30 | 0.03 |
| Band 5 - Near Infrared (NIR) | 850 - 880 | 30 | 3.0 |
| Band 6 - SWIR 1 | 1570 - 1650 | 30 | 8.0  |
| Band 7 - SWIR 2 | 2110 - 2290 | 30 | 18 |
| Band 8 - Panchromatic | 500 - 680 | 15 | 18 |
| Band 9 - Cirrus | 1360 - 1380 | 30 | 2.0 |

### Get to Know Landsat 8 Filenames

When working with Landsat, it is important to understand both the metadata and
the file naming convention. The metadata tell you how the data were processed,
where the data are from and how they are structured.

The file names, tell you what sensor collected the data, the date the data
were collected, and more.

<a href="https://landsat.usgs.gov/what-are-naming-conventions-landsat-scene-identifiers" target="_blank">Landsat file naming convention</a>

<figure>
    <a href="{{ site.url }}/images/courses/earth-analytics/remote-sensing/Collection_FileNameDiffs.png">
    <img src="{{ site.url }}/images/courses/earth-analytics/remote-sensing/Collection_FileNameDiffs.png" alt="landsat file naming convention">
    </a>
    <figcaption>Landsat file names Source: USGS Landsat - <a href="https://landsat.usgs.gov/what-are-naming-conventions-landsat-scene-identifiers
    </figcaption>
</figure>


Let's have a look at one of the files and use the image above to guide us through
understanding the file name.

File: `LC80340322016205LGN00_sr_band1_crop.tif`

| Sensor | Sensor | Satellite | WRS path | WRS row | | | | |
|-------|
| L | C | 8 | 034| 032| 2016 |205 | LGN | 00 |
| Landsat | OLI & TIRS | Landsat 8 | path = 034 | row = 032 | year = 2016 | Julian day= 205 | Ground station: LGN | Archive (first version): 00 |

* L: Landsat
* X: Sensor
  * C = OLI & TIRS
    O = OLI only
    T = IRS only
    E = ETM+
    T = TM
    M = MSS

* S Satelite
* PPP
* RRR
* YYYY = Year
* DDD = Julian DAY of the year
* GSI - Ground station ID
* VV = Archive Version

<a href="http://gisgeography.com/landsat-file-naming-convention/" target="_blank"> More here breaking down the file name.</a>

## Julian Day

In class, we won't spend a lot of time on Julian days. For the purpose of working with Landsat
and MODIS data, what you need to know is that the calendar year Julian day represents
the numeric day of the year. So Jan 1 = day 1. Feb 1 = day 32. And so on.

There are several links at the bottom of this page that provide tables that help
you <a href="https://landweb.modaps.eosdis.nasa.gov/browse/calendar.html" target="_blank">convert Julian days to actual date</a>.


## Landsat tif Files in R

Next, you can open the Landsat data in `R`.



```r
# load spatial packages
library(raster)
library(rgdal)
library(rgeos)

# turn off factors
options(stringsAsFactors = FALSE)
```

If you look at the Landsat directory for the week_07 data, you will see that
each of the individual bands is stored individually as a GeoTIFF rather than
being stored as a stacked or layered, multi-band raster.

Why would they store the data this way?

Conventionally Landsat was stored in a file format called HDF - hierarchical
data format. However that format, while extremely efficient, is a bit more
challenging to work with. In recent years USGS has started to make each band
of a Landsat scene available as a .tif file. This makes it a bit easier to use
across many different programs and platforms.

You have already been working with the geotiff file format in this class! You
will thus use many of the same functions you used previously, to work with Landsat.

## Get List of Files

To begin, let's explore your file directory in `R`, You can use `list.files()` to
grab a list of all files within any directory on your computer.


```r
# get list of all tifs
list.files("data/week-07/landsat/LC80340322016205-SC20170127160728/crop")
## character(0)
```

You can also use `list.files()` with the pattern argument. This allows you to specify
a particular pattern that further subsets your data. In this case, you just want
to look at a list of files with the extension: `.tif`. Note that it is important
that the file **ends with** .tif. So you use the dollar sign at the end of your
pattern to tell `R` to only grab files that end with .tif.

`pattern = ".tif$"`



```r
# but really you just want the tif files
all_landsat_bands <- list.files("data/week-07/landsat/LC80340322016205-SC20170127160728/crop",
                      pattern = ".tif$",
                      full.names = TRUE) # make sure you have the full path to the file
all_landsat_bands
## character(0)
```

Above, you use the `$` after `.tif` to tell `R` to look for files that end with .tif.
This is a good start but there is one more condition that we'd like to meet. We
only want the .tif files that are spectral bands. Notice that some of your files
have text that includes "mask", flags, etc. Those are all additional layers that
you don't need right now. You just need the spectral data saved in bands 1_7.


### Mini Introduction to Regular Expressions

Thus, you want to grab all bands that both end with `.tif` AND contain the text
"band" in them. To do this you use the function `glob2rx()` which allows you to specify
both conditions using what is called regular expressions.

A <a href="https://en.wikipedia.org/wiki/Regular_expression" target = "_blank">regular expression </a> is a sequence of characters that defines a search pattern. Here
you tell `R` to select all files that have the word **band**
in the filename. You use a * sign before and after band because you don't know
exactly what text will occur before or after band. You use `.tif$` to tell `R` that
each file needs to end with `.tif`.



```r
all_landsat_bands <- list.files("data/week-07/landsat/LC80340322016205-SC20170127160728/crop",
           pattern = glob2rx("*band*.tif$"),
           full.names = TRUE) # use the dollar sign at the end to get all files that END WITH
all_landsat_bands
## character(0)
```

## Open the .tif Files in R

Now you have a list of all of the Landsat bands in your folder. You could chose to
open each file individually using the `raster()` function.













