---
layout: single
title: "Create For Loops"
excerpt: "Learn how to write a for loop to process a set of .csv format text files in R. "
authors: ['Leah Wasser', 'Max Joseph']
modified: '2019-09-03'
category: [courses]
class-lesson: ['automating-your-science-r']
permalink: /courses/earth-analytics/automate-science-workflows/create-for-loops-r/
nav-title: 'Create For Loops'
week: 6
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
topics:
  reproducible-science-and-programming: ['literate-expressive-programming', 'functions']
order: 6
redirect_from:
---

{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Write a `for loop` in `R`.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson.

</div>

## Automate Tasks With Loops

In this lesson you will learn how to create loops to perform repeated tasks. Loops
can be combined with functions to create powerful algorithms.

As the name suggests a loop is a sequence of operations that are performed over
and over in some order using a loop `variable`.


```r
for (variable in collection) {
  do things with variable
}
```

You can name the loop `variable` anything you like with a few restrictions:

* the name of the variable cannot start with a number

A few notes about the loop syntax:

1. The loop condition `(variable in collection)` is enclosed in parentheses `()`.
2. The body of the loop is enclosed in curly braces `{ }`.

<i class="fa fa-star" aria-hidden="true"></i>**Data Tip**The curly braces aren't
required for a single-line loop like the one that you created above. However, it is good
practice to always include them.
{: .notice--success }

Below you can see how a `for loop` works. In this case, you provide a vector of
letters. Then you tell `R` to loop through each letter.


```r
# Create a vector of letters called vowels
vowels <- c("a", "e", "i", "o", "u")
# loop through each element in the vector and print out the letter
for (v in vowels) {
  print(v)
}
## [1] "a"
## [1] "e"
## [1] "i"
## [1] "o"
## [1] "u"
```

Here's another loop that repeatedly updates a variable called `len`:


```r
len <- 0
vowels <- c("a", "e", "i", "o", "u")
for (v in vowels) {
  len <- len + 1
  print(len)
}
## [1] 1
## [1] 2
## [1] 3
## [1] 4
## [1] 5
# Number of vowels
len
## [1] 5
```

It's worth tracing the execution of this little program step by step. Since there
are five elements in the vector vowels, the statement inside the loop will be
executed five times. The first time around, `len` is zero (the value assigned to it
before the loop begins) and v is "a". The statement adds 1 to the old value of `len`, producing
1, and updates `len` to refer to that new value. The next time around, v is "e"
and `len` is 1, so `len` is updated to be 2. After three more updates, `len` is 5;
since there is nothing left in the vector vowels for R to process, the loop
finishes.

Note that a loop variable is just a variable that's being used to record progress
in a loop. It still exists after the loop is over, and you can re-use variables
previously defined as loop variables as well:


```r
letter <- "z"
for (letter in c("a", "b", "c")) {
  print(letter)
}
## [1] "a"
## [1] "b"
## [1] "c"
```

## Using Loops to Manipulate Data

Above you covered the basics of how a loop works. Next, let's use a loop to
manipulate some data that you worked with in the first weeks of this course.
To being, let's load libraries that you used for the time series data during week 2.


```r
library(lubridate)
library(ggplot2)
library(dplyr)
```

Next, read in the `/precipitation/805325-precip-daily-2003-2013.csv` file that
contains precipitation data. Fix the date so it's a date class.
















