---
layout: single
title: 'What Is Bash'
excerpt: "This section reviews the importance and benefits of Bash for implementing open reproducible science workflows and for accessing directories and files on your computer."
authors: ['Jenny Palomino', 'Leah Wasser']
category: [courses]
class-lesson: ['bash']
permalink: /courses/intro-to-earth-analytics/bash/intro-bash/
nav-title: "What Is Bash"
dateCreated: 2019-07-15
modified: 2019-07-24
module-title: 'Bash'
module-nav-title: 'Bash'
module-description: 'This chapter explains how Bash can help you implement open reproducible science workflows and introduces useful commands for accessing directories and files on your computer.'
module-type: 'class'
class-order: 1
course: "intro-to-earth-analytics"
week: 2
sidebar:
  nav:
author_profile: false
comments: true
order: 1
topics:
  reproducible-science-and-programming: ['shell']
---
{% include toc title="In This Section" icon="file-text" %}

In this section, you will learn importance and benefits of `Bash` for implementing open reproducible science workflows and for accessing programs and other items on your computer.

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this lesson, you will be able to:

* Explain the roles of `Terminal`, `Shell`, and `Bash` for accessing programs and other items on your computer.


## <i class="fa fa-check-square-o fa-2" aria-hidden="true"></i> What You Need

Be sure that you have completed the instructions on <a href="{{ site.url }}/workshops/setup-earth-analytics-python/setup-git-bash-anaconda/">Setting up Git, Bash, and Anaconda on your computer</a> to install the tools for your operating system (Windows, Mac, Linux). 

 </div>


## Terminal, Shell, and Bash - An Overview

### Terminal

In the early days of computing, the computer that processed data or performed operations was separate from the tool that gave it the instructions to do the processing. There was: 

* The terminal: which was used to send commands to the computer and
* The computer: the hardware that processed the commands

Today, we have computers that can both provide commands AND perform the computation, and these computers have graphical user interfaces (known as GUIs) that make it easy to perform tasks. 

However, accessing the command line or terminal can often be more efficient than using GUIs for certain tasks, and we can send commands via the terminal to programmatically accomplish these tasks. For example, working with files in the terminal is faster and more efficient than working with files in a graphic environment like Windows Explorer or Mac Finder. 

You can also use the terminal to launch and execute open reproducible science tools such as `Jupyter Notebook`, `Python`, and `git`, which you will use throughout this textbook. 

<figure>
 <a href="{{ site.url }}/images/courses/earth-analytics/python-interface/early-terminal.png">
 <img src="{{ site.url }}/images/courses/earth-analytics/python-interface/early-terminal.png" alt = "An image showing a terminal and a computer in the early days of computing."></a>
 <figcaption> Image of an older computer and terminal.</figcaption>
</figure>    

### Shell and Bash

In the chapter on Open Reproducible Science, you learned that `Shell` is the primary program that computers use to receive code (i.e. commands) and return information produced by executing these commands (i.e. output). 

These commands can be entered and executed via the terminal. This allows you to control your computer by typing in commands with a keyboard, instead of using buttons or drop down menus in a GUI with a mouse/keyboard.

`Bash` (also known as the "Bourne-Again Shell") is an implementation of `Shell` and allows you to efficiently perform many tasks. For example, you can use `Bash` to perform operations on multiple files quickly via the command line. 

You can also write and execute scripts in `Bash`, just like you can in `R` or `Python`, that can be executed across different operating systems. 

<i class="fa fa-star"></i> **Data Tip:**  
`Bash` stands for “bourne again shell” and is an updated version of `Shell`. Sometimes you will hear `Bash` and `Shell` used interchangeably; in this course, we will use the term `Bash`.
{: .notice--success}


## Why Is Bash Important for Open Reproducible Science

Using `Bash` in the Terminal is a powerful way of interacting with your computer. GUIs and command line `Bash` are complementary - by knowing both, you will greatly expand the range of tasks you can accomplish with your computer. 

With `Bash` commands, you will be able to perform many tasks more efficiently and automate and replicate workflows across different operating systems. Common tasks that you can run at the command line include checking your current working directory, changing directories, making a new directory, extracting files, and finding files on your computer. 

Working in the terminal with `Bash` provides you with the ability to:
* easily navigate your computer to access and manage files and folders (i.e. directories). 
* quickly and efficiently work with many files and directories at once.
* run programs that provide more functionality at the command line (e.g. `git`).
* launch programs from specific directories on your computer (e.g. `Jupyter Notebook`).
* use repeatable commands for these tasks across many different operating systems (Windows, Mac, Linux).
