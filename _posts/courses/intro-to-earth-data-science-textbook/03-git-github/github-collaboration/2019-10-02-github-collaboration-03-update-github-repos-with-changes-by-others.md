---
layout: single
title: 'Update Your GitHub Repositories With Changes From Others'
excerpt: "GitHub.com . Learn how to update your GitHub repositories with changes by other users."
authors: ['Jenny Palomino', 'Leah Wasser', 'Max Joseph']
category: [courses]
class-lesson: ['git-github-collaboration']
permalink: /courses/intro-to-earth-data-science/git-github/collaboration/update-github-repositories-with-changes-by-others/
nav-title: "Update Your GitHub Repositories"
dateCreated: 2019-09-06
modified: 2019-10-02
module-type: 'class'
course: "intro-to-earth-data-science-textbook"
week: 3
sidebar:
  nav:
author_profile: false
comments: true
order: 3
topics:
  reproducible-science-and-programming: ['git']
---

{% include toc title="On This Page" icon="file-text" %}

<div class='notice--success' markdown="1">

## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives

After completing this page, you will be able to:

* Update your fork of a repository using **GitHub.com**.
* Update your local clone of a repository with changes made in the  **GitHub** repository using `git pull`.

</div>


## Update Your Repository with Changes From Others

When others make in the original repository, you can copy (i.e. pull) those changes to your fork of that repository and then you can copy those changes to the clone on your local computer. 

First, you need to create a pull request on **GitHub.com** to update your fork of the repository from the original repository, and then you need to run the `git pull` command in the Terminal to update your local clone. The following sections review how to complete these steps. 


### Update Your Forked Repo on Github.com

To update your fork on **GitHub.com**, navigate in your web browser to the main **GitHub.com** page of your forked repository: `https://github.com/your-username/example-repository`.

On this web page, create a pull request from the original repository by following these steps:
1. Click on the `New pull request` button to begin the pull request
2. On the new page, choose your fork as the **base fork** and the original repository (e.g. from earthlab-education) as the **head fork**.  This will indicate that the changed files are being requested by your fork (i.e. the base fork) from the original repository (i.e. the head fork). **You will need to click on the text `compare across forks` to be able to update both the base and head forks appropriately.** 
4. Then, click on `Create pull request`.
5. On the new page, click on `Create pull request` once more to finish creating the pull request. 

<figure>
 <a href="{{ site.url }}/images/courses/earth-analytics/git/github-create-reverse-pull-request.gif">
 <img src="{{ site.url }}/images/courses/earth-analytics/git/github-create-reverse-pull-request.gif" alt="You can update your fork with changes made to the original Github repository by creating a pull request from the original repository to your fork."></a>
 <figcaption> You can update your fork with changes made to the original Github repository by creating a pull request from the original repository to your fork. 
 </figcaption>
</figure>

After creating the pull request, you need to merge the pull request, so that the changes in the original repository are copied to your computer. 

You can simply click on the green button for `Merge pull request` and `Confirm merge`. Once you return to the main page of your fork, you will see the changes reflected. 

<figure>
 <a href="{{ site.url }}/images/courses/earth-analytics/git/github-merge-reverse-pull-request.gif">
 <img src="{{ site.url }}/images/courses/earth-analytics/git/github-merge-reverse-pull-request.gif" alt="After creating a pull request, you merge the pull request to apply the changes from the original repository to your fork."></a>
 <figcaption> After creating a pull request, you merge the pull request to apply the changes from the original repository to your fork. 
 </figcaption>
</figure>


### Update Your Local Clone 

To copy the updated files locally to your computer, you can use the Terminal. 

Run the following commands to navigate to the directory that contains your local clone and then to pull down the changes from your updated **GitHub** fork.

```bash
$ cd ~
$ cd earth-analytics
$ cd example-repository
$ git pull
```

Congratulations! You have now updated your local clone with the updates made to the original **GitHub** repository.


For Jenny:
* Need to save copies of all external images using file-names-like-this.png to images/earth-analytics/git-version-control
* Move all images that need it to images/earth-analytics/git-version-control 

