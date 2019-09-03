---
layout: single
title: "Working with Function Arguments"
excerpt: "Learn how to work with function arguments in the R programming language.."
authors: ['Max Joseph', 'Software Carpentry',  'Leah Wasser']
modified: '2019-09-03'
category: [courses]
class-lesson: ['automating-your-science-r']
permalink: /courses/earth-analytics/automate-science-workflows/function-arguments-r/
nav-title: 'Function Arguments'
week: 6
course: "earth-analytics"
sidebar:
  nav:
author_profile: false
comments: true
topics:
  reproducible-science-and-programming: ['literate-expressive-programming', 'functions']
order: 5
redirect_from:
  - "/courses/earth-analytics/week-8/function-arguments-r/"
---


{% include toc title="In This Lesson" icon="file-text" %}



<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this tutorial, you will be able to:

* Define the purpose of a function argument.
* Use default vs. required function arguments in a function.

## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

You will need a computer with internet access to complete this lesson.

</div>

In the previous lessons, you have used many different functions and function
arguments to customize your code.



For example, you used numerous arguments to plot your data including:

1. `main` to add a title.
2. `axes = FALSE` to remove the axes of your plot.
3. `box = FALSE` to remove the box surrounding the plot.

In the example below, you call each argument by name and then assign it a value
based on the type of argument it is. For example the value for the `main = ` argument
is a text string which is the title that you want `R` to add to your plot.














