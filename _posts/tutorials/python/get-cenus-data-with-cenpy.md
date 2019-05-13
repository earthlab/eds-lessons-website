---
layout: single
title: 'Acquiring U.S. census data with Python and cenpy'
date: 2016-06-28
modified: '{:%Y-%m-%d}'.format(datetime.now())
authors: [Zach Schira]
category: [tutorials]
excerpt: 'This tutorial outlines the use of the Cenpy package to search for, and acquire specific census data.'
sidebar:
  nav:
author_profile: false
comments: true
lang: [python]
lib: [pandas, cenpy, pysal]
---
There are several useful online sources for accessing census data provided both by the US census Bureau American Factfinder, and outside sources. These sources, however, are not conducive to large scale data aquisition and analysis. The [Cenpy](https://pypi.python.org/pypi/cenpy/0.9.1) python package allows for programmitic access of this data through the [Census Bureau's API](http://www.census.gov/data/developers/data-sets.html){:data-proofer-ignore=''}.

This tutorial outlines the use of the Cenpy package to search for, and acquire specific census data. Cenpy saves this data as a Pandas dataframe. These dataframes allow for easy access and analysis of data within python. For easy visualization of this data look into the [GeoPandas](http://geopandas.org/) package. This package builds on the base Pandas package to add tools for geospatial data analysis.

## Objectives
- Install Cenpy package
- Search for desired census data
- Download and store data

## Dependencies 

The Cenpy package depends on pandas and requests. 



{:.input}
```python
import pandas as pd
import cenpy as cen
import pysal
```

{:.output}
    /home/max/anaconda3/envs/eds-lessons/lib/python3.6/site-packages/pysal/model/spvcm/abstracts.py:10: UserWarning: The `dill` module is required to use the sqlite backend fully.
      from .sqlite import head_to_sql, start_sql



## Finding Data
The cenpy explorer module allows you to view all of the available [United States Census Bureau API's](http://www.census.gov/data/developers/data-sets.html){:data-proofer-ignore=''}. 

{:.input}
```python
datasets = list(cen.explorer.available(verbose=True).items())

# print first rows of the dataframe containing datasets
pd.DataFrame(datasets).head()
```

{:.output}
{:.execute_result}



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>title</td>
      <td>NONEMP2007                         2007 Nonemp...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>temporal</td>
      <td>NONEMP2007                                    ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>spatial</td>
      <td>NONEMP2007                         United Stat...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>publisher</td>
      <td>NONEMP2007                         U.S. Census...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>programCode</td>
      <td>NONEMP2007                         006:007
POP...</td>
    </tr>
  </tbody>
</table>
</div>





Passing the name of a specific API to `explorer.explain()` will give a description of the data available. For this example, we will use the 2012 American Community Service 1 year data (`2012acs1`).

{:.input}
```python
dataset = '2012acs1'
cen.explorer.explain(dataset)
```

{:.output}
{:.execute_result}



    {'2012 American Community Survey: 1-Year Estimates': "The American Community Survey (ACS) is a nationwide survey designed to provide communities a fresh look at how they are changing. The ACS replaced the decennial census long form in 2010 and thereafter by collecting long form type information throughout the decade rather than only once every 10 years.  Questionnaires are mailed to a sample of addresses to obtain information about households -- that is, about each person and the housing unit itself.  The American Community Survey produces demographic, social, housing and economic estimates in the form of 1-year, 3-year and 5-year estimates based on population thresholds. The strength of the ACS is in estimating population and housing characteristics. It produces estimates for small areas, including census tracts and population subgroups.  Although the ACS produces population, demographic and housing unit estimates,it is the Census Bureau's Population Estimates Program that produces and disseminates the official estimates of the population for the nation, states, counties, cities and towns, and estimates of housing units for states and counties.  For 2010 and other decennial census years, the Decennial Census provides the official counts of population and housing units."}





The base module allows you to establish a connection with the desired API that will be used later to acquire data.

{:.input}
```python
con = cen.base.Connection(dataset)
con
```

{:.output}
{:.execute_result}



    Connection to 2012 American Community Survey: 1-Year Estimates (ID: http://api.census.gov/data/id/2012acs1)





## Acquiring Data

### Geographical specification

Cenpy uses FIPS codes to specify the geographical extent of the data to be downloaded. The object `con` is our connection to the api, and the attribute `geographies` is a dictionary.

{:.input}
```python
print(type(con))
print(type(con.geographies))
print(con.geographies.keys())
```

{:.output}
    <class 'cenpy.remote.APIConnection'>
    <class 'dict'>
    dict_keys(['fips'])



{:.input}
```python
# print head of data frame in the geographies dictionary
con.geographies['fips'].head()
```

{:.output}
{:.execute_result}



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geoLevelId</th>
      <th>name</th>
      <th>optionalWithWCFor</th>
      <th>requires</th>
      <th>wildcard</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>500</td>
      <td>congressional district</td>
      <td>state</td>
      <td>[state]</td>
      <td>[state]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>060</td>
      <td>county subdivision</td>
      <td>NaN</td>
      <td>[state, county]</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>795</td>
      <td>public use microdata area</td>
      <td>NaN</td>
      <td>[state]</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>310</td>
      <td>metropolitan statistical area/micropolitan sta...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>160</td>
      <td>place</td>
      <td>state</td>
      <td>[state]</td>
      <td>[state]</td>
    </tr>
  </tbody>
</table>
</div>





`geo_unit` and `geo_filter` are both necessary arguments for the `query()` function. `geo_unit` specifies the scale at which data should be taken. `geo_filter` then creates a filter to ensure too much data is not downloaded. The following example will download data from all counties in Colorado (state FIPS codes are accessible [here](https://www.mcc.co.mercer.pa.us/dps/state_fips_code_listing.htm)).

{:.input}
```python
g_unit = 'county:*'
g_filter = {'state':'8'}
```

### Specifying variables to extract

The other argument taken by `query()` is cols. This is a list of columns taken from the variables of the API. These variables can be displayed using the `variables` function, however, due to the number of variables it is easier to use the [Social Explorer](https://www.socialexplorer.com/) site to find data you are interested in.

{:.input}
```python
var = con.variables
print('Number of variables in', dataset, ':', len(var))
con.variables.head()
```

{:.output}
    Number of variables in 2012acs1 : 68401



{:.output}
{:.execute_result}



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>concept</th>
      <th>group</th>
      <th>label</th>
      <th>limit</th>
      <th>predicateOnly</th>
      <th>predicateType</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>for</th>
      <td>Census API Geography Specification</td>
      <td>N/A</td>
      <td>Census API FIPS 'for' clause</td>
      <td>0</td>
      <td>True</td>
      <td>fips-for</td>
    </tr>
    <tr>
      <th>in</th>
      <td>Census API Geography Specification</td>
      <td>N/A</td>
      <td>Census API FIPS 'in' clause</td>
      <td>0</td>
      <td>True</td>
      <td>fips-in</td>
    </tr>
    <tr>
      <th>B20005E_045M</th>
      <td>B20005E.  Sex by Work Experience by Earnings f...</td>
      <td>N/A</td>
      <td>Margin of Error for!!Male:!!Other:!!With earni...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>B06004HPR_002M</th>
      <td>B06004HPR.  Place of Birth (White Alone, Not H...</td>
      <td>N/A</td>
      <td>Margin of Error for!!Born in Puerto Rico</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>B24126_438E</th>
      <td>B24126.  Detailed Occupation for the Full-Time...</td>
      <td>N/A</td>
      <td>Multiple machine tool setters, operators, and ...</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>





Related columns of data will always start with the same base prefix, so cenpy has an included function, `varslike`, that will create a list of column names that match the input pattern. It is also useful to add on the `NAME` and `GEOID` columns, as these will provide the name and geographic id of all data. In this example, we will use the [B01001A](https://www.socialexplorer.com/data/ACS2013/metadata/?ds=ACS13&table=B01001A), which gives data for sex by age within the desired geography. The identifier at the end corresponds to males or females of different age groups.

{:.input}
```python
cols = con.varslike('B01001A_')
cols.extend(['NAME', 'GEOID'])
```

With the three necessary arguments, data can be downloaded and saved as a pandas dataframe.

{:.input}
```python
data = con.query(cols, geo_unit=g_unit, geo_filter=g_filter)
# prints a deprecation warning because of how cenpy calls pandas
```

It is useful to replace the default index with the data from the `NAME` or `GEOID` column, as these will give a more useful description of the data.

{:.input}
```python
data.index = data.NAME

# print first five rows and last five columns
data.iloc[:5, -5:]
```

{:.output}
{:.execute_result}



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B01001A_007M</th>
      <th>B01001A_008E</th>
      <th>B01001A_009M</th>
      <th>NAME</th>
      <th>GEOID</th>
    </tr>
    <tr>
      <th>NAME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Adams County, Colorado</th>
      <td>514</td>
      <td>12648</td>
      <td>624</td>
      <td>Adams County, Colorado</td>
      <td>05000US08001</td>
    </tr>
    <tr>
      <th>Arapahoe County, Colorado</th>
      <td>432</td>
      <td>13231</td>
      <td>582</td>
      <td>Arapahoe County, Colorado</td>
      <td>05000US08005</td>
    </tr>
    <tr>
      <th>Boulder County, Colorado</th>
      <td>632</td>
      <td>15297</td>
      <td>189</td>
      <td>Boulder County, Colorado</td>
      <td>05000US08013</td>
    </tr>
    <tr>
      <th>Denver County, Colorado</th>
      <td>389</td>
      <td>15602</td>
      <td>829</td>
      <td>Denver County, Colorado</td>
      <td>05000US08031</td>
    </tr>
    <tr>
      <th>Douglas County, Colorado</th>
      <td>367</td>
      <td>4953</td>
      <td>442</td>
      <td>Douglas County, Colorado</td>
      <td>05000US08035</td>
    </tr>
  </tbody>
</table>
</div>





### Topologically Integrated Geographic Encoding and Referencing (TIGER) data

The Census TIGER API provides geomotries for desired geographic regions. For instance, perhaps we want to have additional information on each county such as area.

{:.input}
```python
cen.tiger.available()
```

{:.output}
{:.execute_result}



    [{'name': 'AIANNHA', 'type': 'MapServer'},
     {'name': 'CBSA', 'type': 'MapServer'},
     {'name': 'Hydro_LargeScale', 'type': 'MapServer'},
     {'name': 'Hydro', 'type': 'MapServer'},
     {'name': 'Labels', 'type': 'MapServer'},
     {'name': 'Legislative', 'type': 'MapServer'},
     {'name': 'Places_CouSub_ConCity_SubMCD', 'type': 'MapServer'},
     {'name': 'PUMA_TAD_TAZ_UGA_ZCTA', 'type': 'MapServer'},
     {'name': 'Region_Division', 'type': 'MapServer'},
     {'name': 'School', 'type': 'MapServer'},
     {'name': 'Special_Land_Use_Areas', 'type': 'MapServer'},
     {'name': 'State_County', 'type': 'MapServer'},
     {'name': 'tigerWMS_ACS2013', 'type': 'MapServer'},
     {'name': 'tigerWMS_ACS2014', 'type': 'MapServer'},
     {'name': 'tigerWMS_ACS2015', 'type': 'MapServer'},
     {'name': 'tigerWMS_ACS2016', 'type': 'MapServer'},
     {'name': 'tigerWMS_ACS2017', 'type': 'MapServer'},
     {'name': 'tigerWMS_ACS2018', 'type': 'MapServer'},
     {'name': 'tigerWMS_Census2010', 'type': 'MapServer'},
     {'name': 'tigerWMS_Current', 'type': 'MapServer'},
     {'name': 'tigerWMS_ECON2012', 'type': 'MapServer'},
     {'name': 'tigerWMS_PhysicalFeatures', 'type': 'MapServer'},
     {'name': 'Tracts_Blocks', 'type': 'MapServer'},
     {'name': 'Transportation_LargeScale', 'type': 'MapServer'},
     {'name': 'Transportation', 'type': 'MapServer'},
     {'name': 'TribalTracts', 'type': 'MapServer'},
     {'name': 'Urban', 'type': 'MapServer'},
     {'name': 'USLandmass', 'type': 'MapServer'}]





First, you must establish a connection to the TIGER API, then you can display the avaialable layers. No Tiger data is available for ACS 2012, so we will use the ACS 2013 for the sake of example, but ideally you will be able to find corresponding Tiger data.

{:.input}
```python
con.set_mapservice('tigerWMS_ACS2013')

# print layers
con.mapservice.layers
```

{:.output}
{:.execute_result}



    {0: (ESRILayer) 2010 Census Public Use Microdata Areas,
     1: (ESRILayer) 2010 Census Public Use Microdata Areas Labels,
     2: (ESRILayer) 2010 Census ZIP Code Tabulation Areas,
     3: (ESRILayer) 2010 Census ZIP Code Tabulation Areas Labels,
     4: (ESRILayer) Tribal Census Tracts,
     5: (ESRILayer) Tribal Census Tracts Labels,
     6: (ESRILayer) Tribal Block Groups,
     7: (ESRILayer) Tribal Block Groups Labels,
     8: (ESRILayer) Census Tracts,
     9: (ESRILayer) Census Tracts Labels,
     10: (ESRILayer) Census Block Groups,
     11: (ESRILayer) Census Block Groups Labels,
     12: (ESRILayer) Unified School Districts,
     13: (ESRILayer) Unified School Districts Labels,
     14: (ESRILayer) Secondary School Districts,
     15: (ESRILayer) Secondary School Districts Labels,
     16: (ESRILayer) Elementary School Districts,
     17: (ESRILayer) Elementary School Districts Labels,
     18: (ESRILayer) Estates,
     19: (ESRILayer) Estates Labels,
     20: (ESRILayer) County Subdivisions,
     21: (ESRILayer) County Subdivisions Labels,
     22: (ESRILayer) Subbarrios,
     23: (ESRILayer) Subbarrios Labels,
     24: (ESRILayer) Consolidated Cities,
     25: (ESRILayer) Consolidated Cities Labels,
     26: (ESRILayer) Incorporated Places,
     27: (ESRILayer) Incorporated Places Labels,
     28: (ESRILayer) Census Designated Places,
     29: (ESRILayer) Census Designated Places Labels,
     30: (ESRILayer) Alaska Native Regional Corporations,
     31: (ESRILayer) Alaska Native Regional Corporations Labels,
     32: (ESRILayer) Tribal Subdivisions,
     33: (ESRILayer) Tribal Subdivisions Labels,
     34: (ESRILayer) Federal American Indian Reservations,
     35: (ESRILayer) Federal American Indian Reservations Labels,
     36: (ESRILayer) Off-Reservation Trust Lands,
     37: (ESRILayer) Off-Reservation Trust Lands Labels,
     38: (ESRILayer) State American Indian Reservations,
     39: (ESRILayer) State American Indian Reservations Labels,
     40: (ESRILayer) Hawaiian Home Lands,
     41: (ESRILayer) Hawaiian Home Lands Labels,
     42: (ESRILayer) Alaska Native Village Statistical Areas,
     43: (ESRILayer) Alaska Native Village Statistical Areas Labels,
     44: (ESRILayer) Oklahoma Tribal Statistical Areas,
     45: (ESRILayer) Oklahoma Tribal Statistical Areas Labels,
     46: (ESRILayer) State Designated Tribal Statistical Areas,
     47: (ESRILayer) State Designated Tribal Statistical Areas Labels,
     48: (ESRILayer) Tribal Designated Statistical Areas,
     49: (ESRILayer) Tribal Designated Statistical Areas Labels,
     50: (ESRILayer) American Indian Joint-Use Areas,
     51: (ESRILayer) American Indian Joint-Use Areas Labels,
     52: (ESRILayer) 113th Congressional Districts,
     53: (ESRILayer) 113th Congressional Districts Labels,
     54: (ESRILayer) 2013 State Legislative Districts - Upper,
     55: (ESRILayer) 2013 State Legislative Districts - Upper Labels,
     56: (ESRILayer) 2013 State Legislative Districts - Lower,
     57: (ESRILayer) 2013 State Legislative Districts - Lower Labels,
     58: (ESRILayer) Census Divisions,
     59: (ESRILayer) Census Divisions Labels,
     60: (ESRILayer) Census Regions,
     61: (ESRILayer) Census Regions Labels,
     62: (ESRILayer) 2010 Census Urbanized Areas,
     63: (ESRILayer) 2010 Census Urbanized Areas Labels,
     64: (ESRILayer) 2010 Census Urban Clusters,
     65: (ESRILayer) 2010 Census Urban Clusters Labels,
     66: (ESRILayer) Combined New England City and Town Areas,
     67: (ESRILayer) Combined New England City and Town Areas Labels,
     68: (ESRILayer) New England City and Town Area Divisions,
     69: (ESRILayer) New England City and Town Area  Divisions Labels,
     70: (ESRILayer) Metropolitan New England City and Town Areas,
     71: (ESRILayer) Metropolitan New England City and Town Areas Labels,
     72: (ESRILayer) Micropolitan New England City and Town Areas,
     73: (ESRILayer) Micropolitan New England City and Town Areas Labels,
     74: (ESRILayer) Combined Statistical Areas,
     75: (ESRILayer) Combined Statistical Areas Labels,
     76: (ESRILayer) Metropolitan Divisions,
     77: (ESRILayer) Metropolitan Divisions Labels,
     78: (ESRILayer) Metropolitan Statistical Areas,
     79: (ESRILayer) Metropolitan Statistical Areas Labels,
     80: (ESRILayer) Micropolitan Statistical Areas,
     81: (ESRILayer) Micropolitan Statistical Areas Labels,
     82: (ESRILayer) States,
     83: (ESRILayer) States Labels,
     84: (ESRILayer) Counties,
     85: (ESRILayer) Counties Labels}





The data retrieved earlier was at the county level, so we will use layer 84. Using the tiger connection, `query()` can retrieve the data, taking the layer and the geographic location as arguments.

{:.input}
```python
geodata = con.mapservice.query(layer=84, where='STATE=8')
```

{:.input}
```python
# preview geodata
geodata.iloc[:5, :5]
```

{:.output}
{:.execute_result}



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AREALAND</th>
      <th>AREAWATER</th>
      <th>BASENAME</th>
      <th>CENTLAT</th>
      <th>CENTLON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4376528327</td>
      <td>25375721</td>
      <td>La Plata</td>
      <td>+37.2863615</td>
      <td>-107.8435627</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8206547707</td>
      <td>4454510</td>
      <td>Saguache</td>
      <td>+38.0807339</td>
      <td>-106.2808607</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1419419128</td>
      <td>3530746</td>
      <td>Sedgwick</td>
      <td>+40.8759564</td>
      <td>-102.3517903</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1003660601</td>
      <td>2035929</td>
      <td>San Juan</td>
      <td>+37.7640122</td>
      <td>-107.6762274</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4605714032</td>
      <td>8166134</td>
      <td>Cheyenne</td>
      <td>+38.8281780</td>
      <td>-102.6034141</td>
    </tr>
  </tbody>
</table>
</div>





This data can now be merged with the original data to create one pandas dataframe containing all of the relevant data.

{:.input}
```python
newdata = pd.merge(data, geodata, left_on='county', right_on='COUNTY')
newdata.iloc[:5, -5:]
```

{:.output}
{:.execute_result}



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>OID</th>
      <th>STATE</th>
      <th>STGEOMETRY.AREA</th>
      <th>STGEOMETRY.LEN</th>
      <th>geometry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>27553700234319</td>
      <td>08</td>
      <td>5.211597e+09</td>
      <td>511817.561207</td>
      <td>POLYGON ((-11644798.3074 4851335.998899996, -1...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>27553703789414</td>
      <td>08</td>
      <td>3.523333e+09</td>
      <td>435243.866171</td>
      <td>(POLYGON ((-11665321.7253 4803086.1294, -11665...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>27553701435070</td>
      <td>08</td>
      <td>3.280834e+09</td>
      <td>291031.607339</td>
      <td>(POLYGON ((-11760745.906 4874953.136100002, -1...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>27553700234321</td>
      <td>08</td>
      <td>6.784688e+08</td>
      <td>341476.209637</td>
      <td>(POLYGON ((-11700783.4396 4811897.626999997, -...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27553711656416</td>
      <td>08</td>
      <td>3.653474e+09</td>
      <td>276727.360768</td>
      <td>POLYGON ((-11674338.3814 4803073.133100003, -1...</td>
    </tr>
  </tbody>
</table>
</div>





