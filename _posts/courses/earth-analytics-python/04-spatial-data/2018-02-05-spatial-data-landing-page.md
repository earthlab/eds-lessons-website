---
layout: single
category: courses
title: "Introduction to Shapefiles and Vector Data in Open Source Python"
permalink: /courses/earth-analytics-python/spatial-data-vector-shapefiles/
week-landing: 4
week: 4
modified: '{:%Y-%m-%d}'.format(datetime.now())
sidebar:
  nav:
comments: false
author_profile: false
course: "earth-analytics-python"
module-type: 'session'
---
{% include toc title="This Week" icon="file-text" %}




<div class="notice--info" markdown="1">

## <i class="fa fa-ship" aria-hidden="true"></i> Welcome to Week {{ page.week }}!

Welcome to week {{ page.week }} of Earth Analytics! This week, you will dive deeper into working with spatial data in `Python`. You will learn how to handle data in different coordinate reference systems, how to create custom maps and legends and how to extract data from a raster file. You are on your way towards integrating many different
types of data into your analysis which involves knowing how to deal with things
like coordinate reference systems and varying data structures.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson and the
spatial-vector-lidar data subset created for the course. Note that the data  download below is large (172MB)
however it contains data that you will use for the next 2 weeks!

{% include/data_subsets/course_earth_analytics/_data-spatial-lidar.md %}


</div>

| Time  | Topic | Speaker |  |  |
|:--------------|:-------|:--------|:-|:-|
| 9:30 AM   | Questions / `Python`   | Leah |  |  |
| 9:45 - 10:15  | Coordinate reference systems & spatial metadata 101 |  |  |  |
| 10:25 - 12:20 | `Python` coding session - spatial data in `Python`  | Leah |  |  |

<!-- 
### 1. Complete the Assignment Below

<div class="notice--warning" markdown="1">

## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Homework (5 points): Due 

### Produce a Report

Create a new `Jupyter Notebook` document. Name it: **lastName-firstInitial-week4.ipynb**
Within your `.ipynb` document, include the plots listed below.

You will submit an `.ipynb` file. Be sure to name your file as instructed above!

In your report, include the plots below. The important part of this week is that you document each step of your workflow using comments. And that you break up the sections of your analysis into SEPARATE code chunks.
 




### Submit to D2L

Submit your report in both `.ipynb` and `.html` format to the D2l week 4 dropbox by 

</div>

## .html Report Structure & Code: 20%

| Full Credit | No Credit  |
|:----|----|
| .ipynb file submitted  |   |   |
| Code is written using "clean" code practices following the Python PEP 8 style guide |  |  |
| First markdown cell contains a title, author and date  | |
| All cells contain code that run   |  |
| All required `Python` packages are listed at the top of the document in a code chunk. |     |


## PLOT: Map of Madera County with Roads 40%

| Full Credit | No Credit  |
|:----|----|
| Roads, plot locations & AOI boundary are included on the map  |   |   |
| Road lines are symbolized by type |  |  |
| Plot location points are symbolized by type | |
| Plots has a title that clearly defines plot contents   |  |
| Plots have a 2-3 sentence caption that clearly describes plot contents |     |
| Plot legend is next to the map (on the side or below) and doesn't overlay the plot contents |     |
| Plot legend is formatted with the correctly symbology that matches the map and is easy to read |     |

## PLOT: Map of Madera County with Roads 30%

| Full Credit | No Credit  |
|:----|----|
| Road length for each county is correct  |   |   |
-->




{:.output}
    file_sizes: 100%|███████████████████████████▉| 210M/211M [00:20<00:00, 12.2MB/s]



## Plot 1 - Roads Map and Legend






{:.output}
{:.display_data}

<figure>

<img src = "{{ site.url }}//images/courses/earth-analytics-python/04-spatial-data/2018-02-05-spatial-data-landing-page_10_0.png" alt = "Map showing the SJER field site roads and plot locations clipped to the site boundary.">
<figcaption>Map showing the SJER field site roads and plot locations clipped to the site boundary.</figcaption>

</figure>






## Plot 2 - Roads in Del Norte, Modoc & Siskiyou Counties in California








{:.output}
{:.display_data}

<figure>

<img src = "{{ site.url }}//images/courses/earth-analytics-python/04-spatial-data/2018-02-05-spatial-data-landing-page_17_0.png" alt = "Map showing the roads layer clipped to the three counties and colored according to which county the road is in.">
<figcaption>Map showing the roads layer clipped to the three counties and colored according to which county the road is in.</figcaption>

</figure>








## Plot 3 - Quantile Map for The USA





{:.output}
{:.display_data}

<figure>

<img src = "{{ site.url }}//images/courses/earth-analytics-python/04-spatial-data/2018-02-05-spatial-data-landing-page_24_0.png" alt = "Total land and total water aggregated by region in the United States.">
<figcaption>Total land and total water aggregated by region in the United States.</figcaption>

</figure>







## Plot 4

You can use the code below to download and unzip the data from the Natural Earth website.
Please note that the download function was written to take

1. a download path - this is the directory where you want to store your data
2. a url - this is the URL where the data are located. The URL below might look odd as it has two "http" strings in it but it is how the url's are organized on natural earth and should work. 

The `download()` function will unzip your data for you and place it in the directory that you specify. 

{:.input}
```python
# Add this line importing the download package to your top cell with the other packages!
from download import download

# Get the data from natural earth
url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries.zip"

# Please note that this is the directory name where your data will be unzipped
download_path = os.path.join("data", "spatial-vector-lidar", "global","ne_10m_admin_0_countries")
download(url, download_path, kind='zip', verbose=False)
country_path = os.path.join(download_path, "ne_10m_admin_0_countries.shp")
```

{:.output}
    file_sizes: 100%|████████████████████████████| 211M/211M [00:40<00:00, 12.2MB/s]
    file_sizes:   0%|                                   | 0.00/4.90M [00:00<?, ?B/s][A
    file_sizes:   0%|                          | 16.4k/4.90M [00:00<00:49, 97.8kB/s][A
    file_sizes:   1%|▏                          | 41.0k/4.90M [00:00<00:40, 119kB/s][A
    file_sizes:   2%|▍                          | 73.7k/4.90M [00:00<00:34, 138kB/s][A
    file_sizes:   2%|▌                           | 106k/4.90M [00:00<00:29, 162kB/s][A
    file_sizes:   3%|▋                           | 131k/4.90M [00:00<00:28, 165kB/s][A
    file_sizes:   4%|█                           | 180k/4.90M [00:00<00:24, 193kB/s][A
    file_sizes:   4%|█▏                          | 213k/4.90M [00:00<00:22, 208kB/s][A
    file_sizes:   5%|█▍                          | 246k/4.90M [00:01<00:21, 213kB/s][A
    file_sizes:   6%|█▌                          | 279k/4.90M [00:01<00:20, 223kB/s][A
    file_sizes:   6%|█▊                          | 311k/4.90M [00:01<00:19, 231kB/s][A
    file_sizes:   7%|█▉                          | 344k/4.90M [00:01<00:22, 202kB/s][A
    file_sizes:   8%|██▎                         | 401k/4.90M [00:01<00:19, 234kB/s][A
    file_sizes:   9%|██▍                         | 434k/4.90M [00:01<00:18, 236kB/s][A
    file_sizes:  10%|██▋                         | 467k/4.90M [00:02<00:18, 235kB/s][A
    file_sizes:  10%|██▊                         | 500k/4.90M [00:02<00:18, 237kB/s][A
    file_sizes:  11%|███                         | 532k/4.90M [00:02<00:17, 244kB/s][A
    file_sizes:  12%|███▏                        | 565k/4.90M [00:02<00:18, 238kB/s][A
    file_sizes:  12%|███▍                        | 598k/4.90M [00:02<00:17, 247kB/s][A
    file_sizes:  13%|███▌                        | 631k/4.90M [00:02<00:17, 240kB/s][A
    file_sizes:  14%|███▊                        | 664k/4.90M [00:02<00:17, 249kB/s][A
    file_sizes:  14%|███▉                        | 696k/4.90M [00:02<00:17, 244kB/s][A
    file_sizes:  15%|████▏                       | 729k/4.90M [00:03<00:17, 239kB/s][A
    file_sizes:  16%|████▎                       | 762k/4.90M [00:03<00:16, 247kB/s][A
    file_sizes:  16%|████▌                       | 795k/4.90M [00:03<00:16, 250kB/s][A
    file_sizes:  17%|████▋                       | 827k/4.90M [00:03<00:17, 238kB/s][A
    file_sizes:  18%|████▉                       | 860k/4.90M [00:03<00:15, 253kB/s][A
    file_sizes:  18%|█████                       | 893k/4.90M [00:03<00:16, 247kB/s][A
    file_sizes:  19%|█████▎                      | 926k/4.90M [00:03<00:16, 235kB/s][A
    file_sizes:  20%|█████▍                      | 958k/4.90M [00:04<00:16, 242kB/s][A
    file_sizes:  20%|█████▋                      | 991k/4.90M [00:04<00:15, 248kB/s][A
    file_sizes:  21%|█████▋                     | 1.02M/4.90M [00:04<00:15, 250kB/s][A
    file_sizes:  22%|█████▊                     | 1.06M/4.90M [00:04<00:16, 238kB/s][A
    file_sizes:  22%|██████                     | 1.09M/4.90M [00:04<00:15, 245kB/s][A
    file_sizes:  23%|██████▏                    | 1.12M/4.90M [00:04<00:15, 250kB/s][A
    file_sizes:  24%|██████▎                    | 1.16M/4.90M [00:04<00:15, 244kB/s][A
    file_sizes:  24%|██████▌                    | 1.19M/4.90M [00:04<00:15, 244kB/s][A
    file_sizes:  25%|██████▋                    | 1.22M/4.90M [00:05<00:15, 238kB/s][A
    file_sizes:  26%|██████▉                    | 1.25M/4.90M [00:05<00:14, 244kB/s][A
    file_sizes:  26%|███████                    | 1.29M/4.90M [00:05<00:14, 249kB/s][A
    file_sizes:  27%|███████▎                   | 1.32M/4.90M [00:05<00:14, 253kB/s][A
    file_sizes:  28%|███████▍                   | 1.35M/4.90M [00:05<00:14, 247kB/s][A
    file_sizes:  28%|███████▋                   | 1.38M/4.90M [00:05<00:14, 243kB/s][A
    file_sizes:  29%|███████▊                   | 1.42M/4.90M [00:05<00:14, 240kB/s][A
    file_sizes:  30%|███████▉                   | 1.45M/4.90M [00:06<00:15, 219kB/s][A
    file_sizes:  30%|████████▏                  | 1.49M/4.90M [00:06<00:13, 247kB/s][A
    file_sizes:  31%|████████▍                  | 1.52M/4.90M [00:06<00:13, 251kB/s][A
    file_sizes:  32%|████████▌                  | 1.56M/4.90M [00:06<00:13, 249kB/s][A
    file_sizes:  32%|████████▊                  | 1.59M/4.90M [00:06<00:13, 249kB/s][A
    file_sizes:  33%|████████▉                  | 1.62M/4.90M [00:06<00:13, 247kB/s][A
    file_sizes:  34%|█████████                  | 1.65M/4.90M [00:06<00:13, 240kB/s][A
    file_sizes:  34%|█████████▎                 | 1.69M/4.90M [00:06<00:13, 246kB/s][A
    file_sizes:  35%|█████████▍                 | 1.72M/4.90M [00:07<00:12, 247kB/s][A
    file_sizes:  36%|█████████▋                 | 1.75M/4.90M [00:07<00:12, 246kB/s][A
    file_sizes:  36%|█████████▊                 | 1.79M/4.90M [00:07<00:12, 242kB/s][A
    file_sizes:  37%|██████████                 | 1.82M/4.90M [00:07<00:12, 248kB/s][A
    file_sizes:  38%|██████████▏                | 1.85M/4.90M [00:07<00:12, 243kB/s][A
    file_sizes:  38%|██████████▍                | 1.88M/4.90M [00:07<00:12, 249kB/s][A
    file_sizes:  39%|██████████▌                | 1.92M/4.90M [00:07<00:12, 244kB/s][A
    file_sizes:  40%|██████████▋                | 1.95M/4.90M [00:08<00:11, 246kB/s][A
    file_sizes:  40%|██████████▉                | 1.98M/4.90M [00:08<00:11, 245kB/s][A
    file_sizes:  41%|███████████                | 2.02M/4.90M [00:08<00:11, 249kB/s][A
    file_sizes:  42%|███████████▎               | 2.05M/4.90M [00:08<00:11, 244kB/s][A
    file_sizes:  42%|███████████▍               | 2.08M/4.90M [00:08<00:11, 244kB/s][A
    file_sizes:  43%|███████████▋               | 2.11M/4.90M [00:08<00:11, 242kB/s][A
    file_sizes:  44%|███████████▊               | 2.15M/4.90M [00:08<00:11, 235kB/s][A
    file_sizes:  44%|████████████               | 2.18M/4.90M [00:08<00:10, 251kB/s][A
    file_sizes:  45%|████████████▏              | 2.21M/4.90M [00:09<00:10, 245kB/s][A
    file_sizes:  46%|████████████▎              | 2.24M/4.90M [00:09<00:10, 250kB/s][A
    file_sizes:  46%|████████████▌              | 2.28M/4.90M [00:09<00:10, 243kB/s][A
    file_sizes:  47%|████████████▋              | 2.31M/4.90M [00:09<00:10, 242kB/s][A
    file_sizes:  48%|████████████▉              | 2.34M/4.90M [00:09<00:10, 247kB/s][A
    file_sizes:  48%|█████████████              | 2.38M/4.90M [00:09<00:10, 243kB/s][A
    file_sizes:  49%|█████████████▎             | 2.41M/4.90M [00:09<00:10, 248kB/s][A
    file_sizes:  50%|█████████████▍             | 2.44M/4.90M [00:10<00:10, 244kB/s][A
    file_sizes:  50%|█████████████▋             | 2.47M/4.90M [00:10<00:09, 246kB/s][A
    file_sizes:  51%|█████████████▊             | 2.51M/4.90M [00:10<00:09, 245kB/s][A
    file_sizes:  52%|█████████████▉             | 2.54M/4.90M [00:10<00:09, 249kB/s][A
    file_sizes:  52%|██████████████▏            | 2.57M/4.90M [00:10<00:10, 231kB/s][A
    file_sizes:  53%|██████████████▎            | 2.61M/4.90M [00:10<00:09, 245kB/s][A
    file_sizes:  54%|██████████████▌            | 2.64M/4.90M [00:10<00:09, 247kB/s][A
    file_sizes:  55%|██████████████▋            | 2.67M/4.90M [00:11<00:09, 246kB/s][A
    file_sizes:  55%|██████████████▉            | 2.70M/4.90M [00:11<00:08, 251kB/s][A
    file_sizes:  56%|███████████████            | 2.74M/4.90M [00:11<00:08, 245kB/s][A
    file_sizes:  57%|███████████████▎           | 2.77M/4.90M [00:11<00:08, 241kB/s][A
    file_sizes:  57%|███████████████▍           | 2.80M/4.90M [00:11<00:08, 238kB/s][A
    file_sizes:  58%|███████████████▌           | 2.83M/4.90M [00:11<00:08, 245kB/s][A
    file_sizes:  59%|███████████████▊           | 2.87M/4.90M [00:11<00:08, 242kB/s][A
    file_sizes:  59%|███████████████▉           | 2.90M/4.90M [00:11<00:08, 247kB/s][A
    file_sizes:  60%|████████████████▏          | 2.93M/4.90M [00:12<00:08, 243kB/s][A
    file_sizes:  61%|████████████████▎          | 2.97M/4.90M [00:12<00:07, 249kB/s][A
    file_sizes:  61%|████████████████▌          | 3.00M/4.90M [00:12<00:08, 236kB/s][A
    file_sizes:  62%|████████████████▋          | 3.03M/4.90M [00:12<00:07, 243kB/s][A
    file_sizes:  63%|████████████████▉          | 3.06M/4.90M [00:12<00:07, 235kB/s][A
    file_sizes:  63%|█████████████████          | 3.10M/4.90M [00:12<00:07, 256kB/s][A
    file_sizes:  64%|█████████████████▏         | 3.13M/4.90M [00:12<00:06, 258kB/s][A
    file_sizes:  65%|█████████████████▍         | 3.16M/4.90M [00:13<00:07, 247kB/s][A
    file_sizes:  65%|█████████████████▌         | 3.19M/4.90M [00:13<00:07, 237kB/s][A
    file_sizes:  66%|█████████████████▊         | 3.23M/4.90M [00:13<00:06, 247kB/s][A
    file_sizes:  67%|█████████████████▉         | 3.26M/4.90M [00:13<00:06, 248kB/s][A
    file_sizes:  67%|██████████████████▏        | 3.29M/4.90M [00:13<00:06, 252kB/s][A
    file_sizes:  68%|██████████████████▎        | 3.33M/4.90M [00:13<00:06, 247kB/s][A
    file_sizes:  69%|██████████████████▌        | 3.36M/4.90M [00:13<00:06, 251kB/s][A
    file_sizes:  69%|██████████████████▋        | 3.39M/4.90M [00:13<00:06, 237kB/s][A
    file_sizes:  70%|██████████████████▊        | 3.42M/4.90M [00:14<00:06, 243kB/s][A
    file_sizes:  71%|███████████████████        | 3.46M/4.90M [00:14<00:05, 249kB/s][A
    file_sizes:  71%|███████████████████▏       | 3.49M/4.90M [00:14<00:05, 236kB/s][A
    file_sizes:  72%|███████████████████▍       | 3.52M/4.90M [00:14<00:05, 243kB/s][A
    file_sizes:  73%|███████████████████▌       | 3.56M/4.90M [00:14<00:05, 240kB/s][A
    file_sizes:  73%|███████████████████▊       | 3.59M/4.90M [00:14<00:05, 246kB/s][A
    file_sizes:  74%|███████████████████▉       | 3.62M/4.90M [00:14<00:05, 245kB/s][A
    file_sizes:  75%|████████████████████▏      | 3.65M/4.90M [00:15<00:05, 244kB/s][A
    file_sizes:  75%|████████████████████▎      | 3.69M/4.90M [00:15<00:04, 249kB/s][A
    file_sizes:  76%|████████████████████▍      | 3.72M/4.90M [00:15<00:04, 239kB/s][A
    file_sizes:  77%|████████████████████▋      | 3.75M/4.90M [00:15<00:04, 254kB/s][A
    file_sizes:  77%|████████████████████▊      | 3.78M/4.90M [00:15<00:04, 239kB/s][A
    file_sizes:  78%|█████████████████████      | 3.82M/4.90M [00:15<00:04, 254kB/s][A
    file_sizes:  79%|█████████████████████▏     | 3.85M/4.90M [00:15<00:04, 242kB/s][A
    file_sizes:  79%|█████████████████████▍     | 3.88M/4.90M [00:15<00:04, 251kB/s][A
    file_sizes:  80%|█████████████████████▌     | 3.92M/4.90M [00:16<00:03, 248kB/s][A
    file_sizes:  81%|█████████████████████▊     | 3.95M/4.90M [00:16<00:03, 243kB/s][A
    file_sizes:  81%|█████████████████████▉     | 3.97M/4.90M [00:16<00:03, 233kB/s][A
    file_sizes:  82%|██████████████████████     | 4.01M/4.90M [00:16<00:03, 244kB/s][A
    file_sizes:  82%|██████████████████████▎    | 4.04M/4.90M [00:16<00:03, 249kB/s][A
    file_sizes:  83%|██████████████████████▍    | 4.07M/4.90M [00:16<00:03, 240kB/s][A
    file_sizes:  84%|██████████████████████▌    | 4.10M/4.90M [00:16<00:03, 251kB/s][A
    file_sizes:  84%|██████████████████████▊    | 4.14M/4.90M [00:16<00:03, 245kB/s][A
    file_sizes:  85%|██████████████████████▉    | 4.17M/4.90M [00:17<00:02, 250kB/s][A
    file_sizes:  86%|███████████████████████▏   | 4.20M/4.90M [00:17<00:02, 245kB/s][A
    file_sizes:  86%|███████████████████████▎   | 4.24M/4.90M [00:17<00:02, 241kB/s][A
    file_sizes:  87%|███████████████████████▌   | 4.27M/4.90M [00:17<00:02, 241kB/s][A
    file_sizes:  88%|███████████████████████▋   | 4.30M/4.90M [00:17<00:02, 245kB/s][A
    file_sizes:  88%|███████████████████████▉   | 4.33M/4.90M [00:17<00:02, 241kB/s][A
    file_sizes:  89%|████████████████████████   | 4.37M/4.90M [00:17<00:02, 238kB/s][A
    file_sizes:  90%|████████████████████████▏  | 4.40M/4.90M [00:18<00:02, 237kB/s][A
    file_sizes:  90%|████████████████████████▍  | 4.43M/4.90M [00:18<00:01, 244kB/s][A
    file_sizes:  91%|████████████████████████▌  | 4.46M/4.90M [00:18<00:01, 249kB/s][A
    file_sizes:  92%|████████████████████████▊  | 4.50M/4.90M [00:18<00:01, 252kB/s][A
    file_sizes:  92%|████████████████████████▉  | 4.53M/4.90M [00:18<00:01, 247kB/s][A
    file_sizes:  93%|█████████████████████████▏ | 4.56M/4.90M [00:18<00:01, 242kB/s][A
    file_sizes:  94%|█████████████████████████▎ | 4.60M/4.90M [00:18<00:01, 248kB/s][A
    file_sizes:  94%|█████████████████████████▌ | 4.63M/4.90M [00:18<00:01, 252kB/s][A
    file_sizes:  95%|█████████████████████████▋ | 4.66M/4.90M [00:19<00:01, 238kB/s][A
    file_sizes:  96%|█████████████████████████▊ | 4.69M/4.90M [00:19<00:00, 244kB/s][A
    file_sizes:  96%|██████████████████████████ | 4.73M/4.90M [00:19<00:00, 250kB/s][A
    file_sizes:  97%|██████████████████████████▏| 4.76M/4.90M [00:19<00:00, 236kB/s][A
    file_sizes:  98%|██████████████████████████▍| 4.79M/4.90M [00:19<00:00, 244kB/s][A
    file_sizes:  98%|██████████████████████████▌| 4.83M/4.90M [00:19<00:00, 248kB/s][A
    file_sizes:  99%|██████████████████████████▊| 4.86M/4.90M [00:19<00:00, 244kB/s][A
    file_sizes: 100%|██████████████████████████▉| 4.89M/4.90M [00:20<00:00, 240kB/s][A



{:.output}
    /Users/leahwasser/anaconda3/envs/earth-analytics-python/lib/python3.6/site-packages/pandas/core/reshape/merge.py:522: UserWarning: merging between different levels can give an unintended result (1 levels on the left, 2 on the right)
      warnings.warn(msg, UserWarning)




{:.output}
{:.display_data}

<figure>

<img src = "{{ site.url }}//images/courses/earth-analytics-python/04-spatial-data/2018-02-05-spatial-data-landing-page_30_0.png" alt = "Natural Earth Global Mean population rank and total estimated population">
<figcaption>Natural Earth Global Mean population rank and total estimated population</figcaption>

</figure>




{:.output}
    
    file_sizes: 100%|███████████████████████████| 4.90M/4.90M [00:39<00:00, 240kB/s][A

