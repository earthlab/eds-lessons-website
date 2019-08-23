---
layout: single
title: "Twitter Data in R Using Rtweet: Analyze and Download Twitter Data"
excerpt: "You can use the Twitter RESTful API to access data about Twitter users and tweets. Learn how to use rtweet to download and analyze twitter social media data in R."
authors: ['Leah Wasser','Carson Farmer']
modified: '2019-08-23'
category: [courses]
class-lesson: ['social-media-r']
permalink: /courses/earth-analytics/get-data-using-apis/use-twitter-api-r/
nav-title: 'Get Tweets - Twitter API'
week: 13
course: "earth-analytics"
module-type: 'class'
sidebar:
  nav:
author_profile: false
comments: true
order: 2
lang-lib:
  r: ['rtweet', 'tidytext', 'dplyr']
topics:
  social-science: ['social-media']
  data-exploration-and-analysis: ['text-mining']
  find-and-manage-data: ['apis', 'find-data']
redirect_from:
   - "/course-materials/earth-analytics/week-12/use-twitter-api-r/"
---


{% include toc title = "In This Lesson" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Query the twitter RESTful API to access and import into `R` tweets that contain various text strings.
* Generate a list of users who are tweeting about a particular topic.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson.

</div>


In this lesson you will explore analyzing social media data accessed from twitter,
in R. You  will use the Twitter RESTful API to access data about both twitter users
and what they are tweeting about

## Getting Started

To get started you'll need to do the following things:

1. Set up a twitter account if you don't have one already.
2. Using your account, setup an application that you will use to access twitter from R
3. Download and install the `rtweet` and `tidytext` packages for R.

Once you've done these things, you are ready to begin querying Twitter's API to
see what you can learn about tweets!

## Set up Twitter App

Let's start by setting up an application in twitter that you can use to access
tweets. To setup your app, follow the documentation from `rtweet` here:

<a href="https://cran.r-project.org/web/packages/rtweet/vignettes/auth.html" target="_blank"><i class="fa fa-info-circle" aria-hidden="true"></i>
 TUTORIAL: How to setup a twitter application using your twitter account</a>

NOTE: you will need to provide your cell phone number to twitter to verify your
use of the API.

<figure>

<img src="{{ site.url }}/images/courses/earth-analytics/week-12/boulder_twitter_map_visualizations.jpg" alt="image showing tweet activity across boulder and denver.">

<figcaption>A heat map of the distribution of tweets across the Denver / Boulder region <a href="http://www.socialmatt.com/amazing-denver-twitter-visualization/" target="_blank">source: socialmatt.com</a></figcaption>
</figure>


## Twitter in R

Once you have your twitter app setup, you are ready to dive into accessing tweets in `R`.

You  will use the `rtweet` package to do this.




```r
# load twitter library - the rtweet library is recommended now over twitteR
library(rtweet)
# plotting and pipes - tidyverse!
library(ggplot2)
library(dplyr)
# text mining library
library(tidytext)
```

The first thing that you need to setup in your code is your authentication. When
you set up your app, it provides you with 3 unique identification elements:

1. appnam
2. key
3. secret

These keys are located in your twitter app settings in the `Keys and Access
Tokens` tab. You will need to copy those into your code as i did below replacing the filler
text that I used in this lesson for the text that twitter gives you in your app.

Next, you need to pass a suite of keys to the API.




```r
# whatever name you assigned to your created app
appname <- "your-app-name"

## api key (example below is not a real key)
key <- "yourLongApiKeyHere"

## api secret (example below is not a real key)
secret <- "yourSecretKeyHere"

```

Finally, you can create a token that authenticates access to tweets!
Note that the authentication process below will open a window in your browser.



```r
# create token named "twitter_token"
twitter_token <- create_token(
  app = appname,
  consumer_key = key,
  consumer_secret = secret,
  access_token = access_token,
  access_secret = access_secret)
```


If authentication is successful works, it should render the following message in
a browser window:

`Authentication complete. Please close this page and return to R.`

### Send a Tweet

Note that your tweet needs to be 140 characters or less.


```r
# post a tweet from R
post_tweet("Look, i'm tweeting from R in my #rstats #earthanalytics class! @EarthLabCU")
## your tweet has been posted!
```

### Search Twitter for Tweets

Now you are ready to search twitter for recent tweets! Let's start by finding all
tweets that use the `#rstats` hashtag. Notice below you use the `rtweet::search_tweets()`
function to search. `search_tweets()` requires the following arguments:

1. **q:** the query word that you want to look for
2. **n:** the number of tweets that you want returned. You can request up to a
maximum of 18,000 tweets.

To see what other arguments you can use with this function, use the `R` help:

`?search_tweets`



```r
## search for 500 tweets using the #rstats hashtag
rstats_tweets <- search_tweets(q = "#rstats",
                               n = 500)
# view the first 3 rows of the dataframe
head(rstats_tweets, n = 3)
## # A tibble: 3 x 90
##   user_id status_id created_at          screen_name text  source
##   <chr>   <chr>     <dttm>              <chr>       <chr> <chr> 
## 1 319314… 11650417… 2019-08-23 23:22:42 gpavolini   Exci… Twitt…
## 2 284964… 11650416… 2019-08-23 23:22:28 gnfrazier   "I w… Twitt…
## 3 368551… 11650415… 2019-08-23 23:21:58 IsabellaGh… To m… Twitt…
## # … with 84 more variables: display_text_width <dbl>,
## #   reply_to_status_id <chr>, reply_to_user_id <chr>,
## #   reply_to_screen_name <chr>, is_quote <lgl>, is_retweet <lgl>,
## #   favorite_count <int>, retweet_count <int>, quote_count <int>,
## #   reply_count <int>, hashtags <list>, symbols <list>, urls_url <list>,
## #   urls_t.co <list>, urls_expanded_url <list>, media_url <list>,
## #   media_t.co <list>, media_expanded_url <list>, media_type <list>,
## #   ext_media_url <list>, ext_media_t.co <list>,
## #   ext_media_expanded_url <list>, ext_media_type <chr>,
## #   mentions_user_id <list>, mentions_screen_name <list>, lang <chr>,
## #   quoted_status_id <chr>, quoted_text <chr>, quoted_created_at <dttm>,
## #   quoted_source <chr>, quoted_favorite_count <int>,
## #   quoted_retweet_count <int>, quoted_user_id <chr>,
## #   quoted_screen_name <chr>, quoted_name <chr>,
## #   quoted_followers_count <int>, quoted_friends_count <int>,
## #   quoted_statuses_count <int>, quoted_location <chr>,
## #   quoted_description <chr>, quoted_verified <lgl>,
## #   retweet_status_id <chr>, retweet_text <chr>,
## #   retweet_created_at <dttm>, retweet_source <chr>,
## #   retweet_favorite_count <int>, retweet_retweet_count <int>,
## #   retweet_user_id <chr>, retweet_screen_name <chr>, retweet_name <chr>,
## #   retweet_followers_count <int>, retweet_friends_count <int>,
## #   retweet_statuses_count <int>, retweet_location <chr>,
## #   retweet_description <chr>, retweet_verified <lgl>, place_url <chr>,
## #   place_name <chr>, place_full_name <chr>, place_type <chr>,
## #   country <chr>, country_code <chr>, geo_coords <list>,
## #   coords_coords <list>, bbox_coords <list>, status_url <chr>,
## #   name <chr>, location <chr>, description <chr>, url <chr>,
## #   protected <lgl>, followers_count <int>, friends_count <int>,
## #   listed_count <int>, statuses_count <int>, favourites_count <int>,
## #   account_created_at <dttm>, verified <lgl>, profile_url <chr>,
## #   profile_expanded_url <chr>, account_lang <lgl>,
## #   profile_banner_url <chr>, profile_background_url <chr>,
## #   profile_image_url <chr>
```

## Retweets

A retweet is when you or someone else shares someone elses tweet so your / their
followers can see it. It is similar to sharing in Facebook where you can add a
quote or text above the retweet if you want or just share the post. Let's use
the same query that you used above but this time ignore all retweets by setting
the `include_rts` argument to `FALSE`. You can get tweet / retweet stats from
your dataframe, separately.


```r
# find recent tweets with #rstats but ignore retweets
rstats_tweets <- search_tweets("#rstats", n = 500,
                             include_rts = FALSE)
# view top 2 rows of data
head(rstats_tweets, n = 2)
## # A tibble: 2 x 90
##   user_id status_id created_at          screen_name text  source
##   <chr>   <chr>     <dttm>              <chr>       <chr> <chr> 
## 1 943852… 11650394… 2019-08-23 23:13:35 zoedottxt   "A y… Twitt…
## 2 211937… 11650381… 2019-08-23 23:08:36 toddrjones  "Ano… Twitt…
## # … with 84 more variables: display_text_width <dbl>,
## #   reply_to_status_id <chr>, reply_to_user_id <chr>,
## #   reply_to_screen_name <chr>, is_quote <lgl>, is_retweet <lgl>,
## #   favorite_count <int>, retweet_count <int>, quote_count <int>,
## #   reply_count <int>, hashtags <list>, symbols <list>, urls_url <list>,
## #   urls_t.co <list>, urls_expanded_url <list>, media_url <list>,
## #   media_t.co <list>, media_expanded_url <list>, media_type <list>,
## #   ext_media_url <list>, ext_media_t.co <list>,
## #   ext_media_expanded_url <list>, ext_media_type <chr>,
## #   mentions_user_id <list>, mentions_screen_name <list>, lang <chr>,
## #   quoted_status_id <chr>, quoted_text <chr>, quoted_created_at <dttm>,
## #   quoted_source <chr>, quoted_favorite_count <int>,
## #   quoted_retweet_count <int>, quoted_user_id <chr>,
## #   quoted_screen_name <chr>, quoted_name <chr>,
## #   quoted_followers_count <int>, quoted_friends_count <int>,
## #   quoted_statuses_count <int>, quoted_location <chr>,
## #   quoted_description <chr>, quoted_verified <lgl>,
## #   retweet_status_id <chr>, retweet_text <chr>,
## #   retweet_created_at <dttm>, retweet_source <chr>,
## #   retweet_favorite_count <int>, retweet_retweet_count <int>,
## #   retweet_user_id <chr>, retweet_screen_name <chr>, retweet_name <chr>,
## #   retweet_followers_count <int>, retweet_friends_count <int>,
## #   retweet_statuses_count <int>, retweet_location <chr>,
## #   retweet_description <chr>, retweet_verified <lgl>, place_url <chr>,
## #   place_name <chr>, place_full_name <chr>, place_type <chr>,
## #   country <chr>, country_code <chr>, geo_coords <list>,
## #   coords_coords <list>, bbox_coords <list>, status_url <chr>,
## #   name <chr>, location <chr>, description <chr>, url <chr>,
## #   protected <lgl>, followers_count <int>, friends_count <int>,
## #   listed_count <int>, statuses_count <int>, favourites_count <int>,
## #   account_created_at <dttm>, verified <lgl>, profile_url <chr>,
## #   profile_expanded_url <chr>, account_lang <lgl>,
## #   profile_banner_url <chr>, profile_background_url <chr>,
## #   profile_image_url <chr>
```

Next, let's figure out who is tweeting about `R` using the `#rstats` hashtag.


```r
# view column with screen names - top 6
head(rstats_tweets$screen_name)
## [1] "zoedottxt"       "toddrjones"      "CRANberriesFeed" "CRANberriesFeed"
## [5] "CRANberriesFeed" "CRANberriesFeed"
# get a list of unique usernames
unique(rstats_tweets$screen_name)
##   [1] "zoedottxt"       "toddrjones"      "CRANberriesFeed"
##   [4] "AntoViral"       "waterlego"       "gp_pulipaka"    
##   [7] "quaesita"        "certifiedwaif"   "dataclaudius"   
##  [10] "DerFredo"        "rocitations"     "Rbloggers"      
##  [13] "tidyversetweets" "grrrck"          "BGravesteijn"   
##  [16] "westgatecology"  "ChasingMicrobes" "Mayacelium"     
##  [19] "UrbanDemog"      "shamindraas"     "markvdloo"      
##  [22] "AvrahamAdler"    "hwericsatie"     "ethantenison"   
##  [25] "Rei780"          "StrictlyStat"    "Xtophe_Bontemps"
##  [28] "wia_conference"  "CareQualityComm" "volha_tryputsen"
##  [31] "alexsussuarana"  "W_R_Chase"       "_ColinFay"      
##  [34] "KathleenWendt8"  "Hec_Garrido"     "rui_barros17"   
##  [37] "HarryASmith9002" "c_borstell"      "causalinf"      
##  [40] "rweekly_live"    "astaples_mi"     "researchcommunK"
##  [43] "Ceo_Branding"    "packpridejones"  "rmflight"       
##  [46] "PodsProgram"     "MarkShadden1"    "sellorm"        
##  [49] "abresler"        "theRcast"        "pachamaltese"   
##  [52] "EarlybirdDev"    "LVKremin"        "topepos"        
##  [55] "rinpharma"       "realauggiehesch" "TazPoltorak"    
##  [58] "nyhackr"         "thomas_mock"     "CKVanPay"       
##  [61] "CivicAngela"     "andrew_leach"    "hadleywickham"  
##  [64] "rstatsdata"      "gavinprm"        "SteveGawthorpe" 
##  [67] "WhitneyEpi"      "gRizzStats"      "hutchins_e"     
##  [70] "d_olivaw"        "lemuscanovas"    "cliffbeall"     
##  [73] "thinksysinc"     "DataDaft"        "tladeras"       
##  [76] "DaveParr"        "RLangTip"        "LeafyEricScott" 
##  [79] "Ektropos"        "DogmaticPrior"   "TiffanyTimbers" 
##  [82] "morgsbrew"       "oscar_b123"      "matloff"        
##  [85] "TimoRoettger"    "rfortherest"     "BGSA_WSU"       
##  [88] "RenRidesCycles"  "mattwilkinsbio"  "ChavarriaMinera"
##  [91] "DrKAinslie"      "nielsberglund"   "haematobot"     
##  [94] "MicheleTobias"   "S_bravo"         "crcgrubbsd"     
##  [97] "gbganalyst"      "UK_PetDogPop"    "TAlexPerkins"   
## [100] "antoine_fabri"   "LIBDrstats"      "scottyd22"      
## [103] "LMSaxhaug"       "WesongaRonald"   "juliesquid"     
## [106] "lyderhermansen"  "JonTheGeek"      "mishafredmeyer" 
## [109] "rstatsdc"        "StatGarrett"     "TroyFor25"      
## [112] "CougRstats"      "R4DScommunity"   "gboeing"        
## [115] "whipson3"        "eric_layland"    "walkabilly"     
## [118] "uHITbaseball"    "uwepidemiology"  "rcentrrall"     
## [121] "r_and_omics"     "KatheMathBio"    "FelixEVargas"   
## [124] "katiesegreti"    "Escells"         "PghAdventurer"  
## [127] "phileas_c"       "AedinCulhane"    "brentocarrigan" 
## [130] "DustinStoltz"    "jesseberger"     "javierluraschi" 
## [133] "Visokio"         "taraskaduk"      "PipeFunction"   
## [136] "iprophage"       "julianlavila"    "ejmarenco1"     
## [139] "dataandme"       "dataelixir"      "adababbage"     
## [142] "HakimAbdi"       "bradleyboehmke"  "CLaunderer"     
## [145] "jaseziv"         "mdancho84"       "swricci"        
## [148] "grimbough"       "nstrande"        "humeursdevictor"
## [151] "dgkeyes"         "dr_keithmcnulty" "nevromeCS"      
## [154] "tylermorganwall" "StatsCloud"      "o_gonzales"     
## [157] "alexandregeorg5" "WeAreRLadies"    "ChrisLavoieEcon"
## [160] "rick_pack2"      "torkildl"        "OutboxHub"      
## [163] "caprico_aries"   "jtrecenti"       "josh_longbottom"
## [166] "RhinoEcologist"  "carlcarrie"      "coolbutuseless" 
## [169] "LandbouLisa"     "ludictech"       "milos_agathon"  
## [172] "afunguy95"       "cimentadaj"      "CillianMacAodh" 
## [175] "thegymnosophist" "YousriMarzouki"  "FedericoRG"     
## [178] "OCGTraining"     "nosimpler_me"    "RLangPackage"   
## [181] "JenRichmondPhD"  "claudiodanielpc" "mattthereed"    
## [184] "aschinchon"      "luhugerth"       "mmeierer"       
## [187] "AtlanHQ"         "zx8754"          "appsilon"       
## [190] "TraineeGeek"     "AndreaCirilloAC" "LearnRinaDay"   
## [193] "swcarpentry_ja"  "martin_rstats"   "calvinmdewilde" 
## [196] "guangchuangyu"   "klmr"            "CherguiSafouane"
## [199] "bjoern_walther"  "SurfingSiren"    "GEMReport"      
## [202] "mauro_lepore"    "AriyoOludare"    "thomasp85"      
## [205] "grssnbchr"       "Adrowitzer"      "THEAdamGabriel" 
## [208] "angelozehr"      "kurzanovart"     "zkajdan"        
## [211] "InsectEcology"   "Vdot_Spain"      "KWBerlin_R"     
## [214] "kiwiskiNZ"       "r4n4m4hmud"      "lee_hawthorn"   
## [217] "foundinblank"    "verajosemanuel"  "rstudio"        
## [220] "siminaboca"      "GilesDJones"     "RLadiesMTL"     
## [223] "BlasBenito"      "alexpghayes"     "nathanodgers"   
## [226] "MarkGingrass"    "KirkDBorne"      "EthanGoan"      
## [229] "ramez_s"         "sharlagelfand"   "BiodiversityGuy"
## [232] "daily_r_sheets"  "hellomista"      "PM_maths"       
## [235] "ArseneXie"       "johncassil"      "ThomasVConti"   
## [238] "howardsfriedman" "tsonika"         "migueldva"      
## [241] "Gabriel00602805" "megmwheeler"     "terusterang__"  
## [244] "petra_kuhnert"   "SouMyajiT_RO"    "michael_wiebe"  
## [247] "sckottie"        "JezRoff"         "Mooniac"        
## [250] "gjmount"         "BenjaminWolfe"   "alistaire"      
## [253] "yabellini"       "RLadies_rciacte" "hessandrea"     
## [256] "roamingmoth"     "juliasilge"      "kburnswrites"   
## [259] "jamie_lendrum"   "healthstatsdude" "bigagdata"      
## [262] "NathanMicatka"   "brad_weiner"     "ClausWilke"     
## [265] "DataSciEng"      "sarahdolson"     "gabbspalomo"    
## [268] "dvaughan32"      "JDHaltigan"      "JanaJarecki"    
## [271] "MariannaFoos"    "NCrouch89"       "_willdebras"    
## [274] "DethWench"       "GeoMaisonobe"    "SeanfromSeabeck"
## [277] "chainsawriot"    "jonsweetman"     "etmckinley"     
## [280] "DataSciSalon"    "leach_jim"       "Stat_Ron"       
## [283] "GuyProchilo"     "SaanpaurSeedi"   "TenderIsTheByte"
## [286] "joranelias"      "serdarbalci"     "krlmlr"         
## [289] "mjhendrickson"   "mribeirodantas"  "strnr"          
## [292] "PyData"          "prec_analytics"  "dunn_sam"       
## [295] "jozefhajnala"
```

You  can similarly use the `search_users()` function to just see what users are tweeting
using a particular hashtag. This function returns just a data.frame of the users
and information about their accounts.


```r
# what users are tweeting with #rstats
users <- search_users("#rstats",
                      n = 500)
# just view the first 2 users - the data frame is large!
head(users, n = 2)
## # A tibble: 2 x 90
##   user_id status_id created_at          screen_name text  source
##   <chr>   <chr>     <dttm>              <chr>       <chr> <chr> 
## 1 961691… 11641739… 2019-08-21 13:54:45 FC_rstats   This… Twitt…
## 2 101181… 11650389… 2019-08-23 23:11:52 rstatstweet "Ano… rstat…
## # … with 84 more variables: display_text_width <dbl>,
## #   reply_to_status_id <chr>, reply_to_user_id <chr>,
## #   reply_to_screen_name <chr>, is_quote <lgl>, is_retweet <lgl>,
## #   favorite_count <int>, retweet_count <int>, quote_count <int>,
## #   reply_count <int>, hashtags <list>, symbols <list>, urls_url <list>,
## #   urls_t.co <list>, urls_expanded_url <list>, media_url <list>,
## #   media_t.co <list>, media_expanded_url <list>, media_type <list>,
## #   ext_media_url <list>, ext_media_t.co <list>,
## #   ext_media_expanded_url <list>, ext_media_type <chr>,
## #   mentions_user_id <list>, mentions_screen_name <list>, lang <chr>,
## #   quoted_status_id <chr>, quoted_text <chr>, quoted_created_at <dttm>,
## #   quoted_source <chr>, quoted_favorite_count <int>,
## #   quoted_retweet_count <int>, quoted_user_id <chr>,
## #   quoted_screen_name <chr>, quoted_name <chr>,
## #   quoted_followers_count <int>, quoted_friends_count <int>,
## #   quoted_statuses_count <int>, quoted_location <chr>,
## #   quoted_description <chr>, quoted_verified <lgl>,
## #   retweet_status_id <chr>, retweet_text <chr>,
## #   retweet_created_at <dttm>, retweet_source <chr>,
## #   retweet_favorite_count <int>, retweet_retweet_count <int>,
## #   retweet_user_id <chr>, retweet_screen_name <chr>, retweet_name <chr>,
## #   retweet_followers_count <int>, retweet_friends_count <int>,
## #   retweet_statuses_count <int>, retweet_location <chr>,
## #   retweet_description <chr>, retweet_verified <lgl>, place_url <chr>,
## #   place_name <chr>, place_full_name <chr>, place_type <chr>,
## #   country <chr>, country_code <chr>, geo_coords <list>,
## #   coords_coords <list>, bbox_coords <list>, status_url <chr>,
## #   name <chr>, location <chr>, description <chr>, url <chr>,
## #   protected <lgl>, followers_count <int>, friends_count <int>,
## #   listed_count <int>, statuses_count <int>, favourites_count <int>,
## #   account_created_at <dttm>, verified <lgl>, profile_url <chr>,
## #   profile_expanded_url <chr>, account_lang <lgl>,
## #   profile_banner_url <chr>, profile_background_url <chr>,
## #   profile_image_url <chr>
```

Let's learn a bit more about these people tweeting about `R`. First, where are
they from?


```r
# how many locations are represented
length(unique(users$location))
## [1] 312

users %>%
  ggplot(aes(location)) +
  geom_bar() + coord_flip() +
      labs(x = "Count",
      y = "Location",
      title = "Twitter users - unique locations ")
```

<img src="{{ site.url }}/images/courses//earth-analytics-r/13-programmatic-data-access/in-class/2017-04-19-social-media-02-use-r-twitter-api/explore-users-1.png" title="plot of users tweeting about R" alt="plot of users tweeting about R" width="90%" />

Let's sort by count and just plot the top locations. To do this, you use top_n().
Note that in this case you are grouping your data by user. Thus top_n() will return
locations with atleast 15 users associated with it.


```r
users %>%
  count(location, sort = TRUE) %>%
  mutate(location = reorder(location, n)) %>%
  top_n(20) %>%
  ggplot(aes(x = location, y = n)) +
  geom_col() +
  coord_flip() +
      labs(x = "Count",
      y = "Location",
      title = "Where Twitter users are from - unique locations ")
```

<img src="{{ site.url }}/images/courses//earth-analytics-r/13-programmatic-data-access/in-class/2017-04-19-social-media-02-use-r-twitter-api/users-tweeting-1.png" title="top 15 locations where people are tweeting" alt="top 15 locations where people are tweeting" width="90%" />

It looks like you have some `NA` or no data values in your list. Let's remove those
with `na.omit()`.


```r
users %>%
  count(location, sort = TRUE) %>%
  mutate(location = reorder(location,n)) %>%
  na.omit() %>%
  top_n(20) %>%
  ggplot(aes(x = location,y = n)) +
  geom_col() +
  coord_flip() +
      labs(x = "Location",
      y = "Count",
      title = "Twitter users - unique locations ")
```

<img src="{{ site.url }}/images/courses//earth-analytics-r/13-programmatic-data-access/in-class/2017-04-19-social-media-02-use-r-twitter-api/users-tweeting2-1.png" title="top 15 locations where people are tweeting - na removed" alt="top 15 locations where people are tweeting - na removed" width="90%" />

Looking at your data, what do you notice that might improve this plot?
There are 314 unique locations in your list. However, everyone didn't specify their
locations using the approach. For example some just identified their country:
United States for example and others specified a city and state. You may want to
do some cleaning of these data to be able to better plot this distribution - especially
if you want to create a map of these data!

### Users by Time Zone

Let's have a look at the time zone field next.



```r
users %>% na.omit() %>%
  ggplot(aes(time_zone)) +
  geom_bar() + coord_flip() +
      labs(x = "Count",
      y = "Time Zone",
      title = "Twitter users - unique time zones ")
```

<div class="notice--warning" markdown="1">

## <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Optional Challenge

Use the example above, plot users by time zone. List time zones that have at least
20 users associated with them. What do you notice about the data?
</div>



The plots above aren't perfect. What do you start to notice about working
with these data? Can you simply download them and plot the data?

## Data munging  101

When you work with data from sources like NASA, USGS, etc. there are particular
cleaning steps that you often need to do. For instance:

* you may need to remove nodata values
* you may need to scale the data
* and others

In the next lesson, you will dive deeper into the art of "text-mining" to extract
information about a particular topic from twitter.


<div class="notice--info" markdown="1">

## Additional Resources

* <a href="http://tidytextmining.com/" target="_blank">Tidy text mining online book</a>
* <a href="https://mkearney.github.io/rtweet/articles/intro.html#retrieving-trends" target="_blank">A great overview of the rtweet package by Mike Kearny</a>
* <a href="https://francoismichonneau.net/2017/04/tidytext-origins-of-species/" target="_blank">A blog post on tidytext by Francois Michonneau</a>
*  <a href="https://blog.twitter.com/2008/what-does-rate-limit-exceeded-mean-updated" target="_blank">About the twitter API rate limit</a>

</div>
