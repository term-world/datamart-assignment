
| Date              |          |
|:------------------|:---------|
| `TODO` | Assigned |
| Various (see below)    | Due      |
| Status            | [![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml) |

# GLORIOUS NEW DATA PROJECT ON HORIZON! FUTURE OF `term-world` LOOKING BRIGHTER THAN EVER!

**Reported by `Official Mayor-Endorsed News` on `TODO`**

Welcome to the inaugural report from `Official Mayor-Endorsed News`!
Given the recent defunding and dissolution of TNN following last week's
egregious journalistic debacle involving what our Mayor calls "fake
news", the `Official Mayor-Endorsed News` is here to ensure all the
fair citizens of `term-world` stay informed of the exciting new
developments our Mayor has in store for our community!

And we have some exciting news to share regarding one of the most
ambitious projects to be proposed by our Mayor! But why take our word
for it, when you could hear about this new endeavor directly from our
Mayor! In an exclusive interview with `Official Mayor-Endorsed News`,
our Mayor had the below information to share!

"Your Mayor here with a new proposal sure to inspire you all to new
levels of greatness! I've recently learned that this thing called 'Big
Data' is *all* the talk outside `term-world`, and I--your Mayor--am
here to say it's time we brought it to our incredible community!"

The newly constructed `datamart` will house *all* manner of data science
projects meant to collect and synthesize the latest data on the fair
citizens of `term-world`! As per usual, our Mayor is counting on *YOU*
to help his vision of a `term-world` up-to-date with all the latest
"Big Data" trends become a reality!

## Overview

In this set of activities we cover:

* working collaboratively using Github
* branching
* merging
* issuing "Pull Requests"
* exploring `data structures`, namely `list`s, a Python feature which:
  * allows storage of many values in one variable
  * organizes itself by _indexes_ (that is, numerical "addresses")
  * is _mutable_ (can be changed), which means it can expand or contract
* a review of `method`s: features of Python objects which act like "powers" of a given _kind_ of object

You'll complete a few tasks:

* collecting and entering data from various neighborhoods
* organizing collected data
* doing basic data analysis with collected data

## Previous Learning Objectives

If you wish to review previous learning objectives from our assignments, you can visit the [`Syllabus`](https://chompe.rs/100-syllabus) for helpful information. However, it's also important to make an effort to retain what we have covered thus far as we progress through the course sections of the Readme might be taken out.

## Completing the `datamart`

This assignment has four main parts:

1. Collecting data
2. Writing a program to analyze the data
3. Compiling a report which discusses results of the analysis
4. Individual reflection on the activity

This work is due at different times. The following table outlines due dates:

|Date |Item due |
|:----|:--------|
|`TODO` |Survey and responses |
|`TODO`|Analysis and results (including programming) |

Should everyone be in a position to proceed with other assignment sections earlier, we will do so.

### Collecting data

Your neighborhood must develop an eight (8) question survey that you will deliver to other neighborhoods in order to collect their responses. Choose two (2) questions from each of the categories below. At least one (1) question in each category _must be_ of the "ranked" type. Your group should add these questions to the form assigned to and shared with your neighborhood.

Once you've conducted your survey (see above table for due dates), transfer your results to the spreadsheet shared with your neighborhood. Identify the questions asked on your survey by renaming the `Q` columns with the ID of the corresponding question from the table(s) below. Once completed, your elected neighborhood leader should:

* export survey results as a spreadsheet and transfer to your neighborhood's template
* `upload` the file to the `data` directory of this repository
* create a `Pull Request`
* successfully appeal to neighbors to approve it
* `merge` the `Pull Request` into `main`

#### Developing a neighborhood-specific question

Neighborhoods are allowed to (but do not _have_ to) develop one (1) question to ask as a replacement for a required question selected from the list below. However, it must belong to one of the four categories. Identify this question as question `G` in your responses spreadsheet for the category to which it is added.

This question must be approved by the Mayoral staff. If your neighborhood elects to write a question, add it below:

|ID|Type|Question|
|:-|:---|:-------|
|`TODO`|`TODO`|`TODO`|

#### Questions

|ID|Type |Question |
|:-|:----|:--------|
|**Perception**     |
|1A|`Ranked` |Using `term-world` is easy |
|1B|`Ranked` |The actions the Mayor's office takes are transparent |
|1C|`Ranked` |I feel like my work is secure in `term-world` |
|1D|`Ranked` |I receive reasonbly high value for my effort on projects in `term-world` |
|1E|`Free-response`|I would describe `term-world` as...|
|1F|`Free-response`|I think everyone else in at least my neighorhood sees `term-world` as...|
|**Quality of life** |
|2A|`Ranked` |I feel like my work in `term-world` _does something_ (has efficacy) |
|2B|`Ranked` |`term-world` is a joyous place to work |
|2C|`Ranked` |I'm proud to be a citizen of `term-world` |
|2D|`Ranked` |I would rate my overall satsifaction with living in `term-world` very highly|
|2E|`Free-response` |The most frustrating feature in `term-world` is...|
|2F|`Free-response` |The feature of `term-world` that makes my life better is...|
|**World services**|
|3A|`Ranked` |Things in `term-world` work more often than not |
|3B|`Ranked` |I'm able to access `term-world` on a regular basis, no matter where I am |
|3C|`Ranked` |I enjoy working with Mayoral staff |
|3D|`Ranked` |I feel that the Mayoral staff is helpful and interested in me as as citizen |
|3E|`Free-response` |One mechanism that would make life in `term-world` better is...|
|3F|`Free-response` |A mechanism that would be _cool_ to see might be...|
|**Inclusivity and community**|
|4A|`Ranked`|I feel like I can and do participate in my neighborhood; I feel included |
|4B|`Ranked`|My neighborhood is a community to which everyone contributes roughly equally |
|4C|`Ranked`|The Mayoral staff treats me and everyone in my neighborhood with respect |
|4D|`Ranked`|If I have trouble with something, the suggestions I get from my neighbors really help me |
|4E|`Free-response`|A policy which might make inclusivity and community stronger is...|
|4F|`Free-response`|If communities could have more power, one thing they'd be able to do is...|

##### Ranked questions

Some questions contemplate a ranking system using values `1`-`5` to represent certain responses where:

* `1`: Disagree Strongly
* `5`: Agree Strongly

##### Free-response questions

Free respose questions are designed for short answers of no more than 2-5 words. These questions, being open-end, are intended to provide suggestions to the Mayor's Office for improvement.

### Analyzing data

Data analysis is the programmatic part of this assignment. Here, you'll be asked to work in [`analyzer/main.py`](analyzer/main.py) to find ways to chop, sort, and otherwise understand the data. To do this, you'll need to build some tools in the form of `function`s that handle `list`s. Here's a minimum of what you'll need to build:

|Function name |Parameters  |Return type | Description                                               |
|:-------------|:-----------|:-----------|:----------------------------------------------------------|
|get_row       |`int`       |`list`      |Returns a chosen row of the table as a `list`              |
|counter       |`str`       |`int`       |Counts instances (across all data) of the `str` entered as a parameter, returns count of that `str` |
|avg_column    |`str`       |`float`     |Takes column name as parameter and averages the contents of that column |
|min_value     |`str`       |`int`       |Takes column name as parameter and finds the minimum value in that column |
|max_value     |`str`       |`int`       |Takes column name as parameter and finds the maximum value in that column |
|get_mode      |`str`       |`int`       |Takes column name as parameter and finds the mode of the column's data |
|get_median    |`str`       |`int`       |Takes column name as parameter and finds the median of the column's data |

### Writing

### Neigborhood Evaluation Research Diagnostic report

This report assumes group participation, and only requires `1` copy. Neighborhood members should collaborate on this report, as it requests many different viewpoints in order to successfully represent your neighborhood.

### Individual reflection

This assignment also requires an individual reflection, completed by _copying_ the `reflection.md` document and renaming it `reflection-USERNAME.md` to differentiate your answers from others.

## Improvement suggestions

Here are some suggestions for improvements you can, **but are not limited to** use:

|Improvement Suggestions |Description                                |
|:--------------------|:---------------------------------------------|                
| Lists |Sort by multiple columns |      
| Lists |Ability to update the contents of a given cell (e.g. to fix a typo) |
| Lists |Ability to update multiple cells with a formula (e.g. normalize data) |
| Lists |Ability to prompt user to save changes if data has been altered since last operation|
| Lists, iteration | Other forms of data analysis not implemented in the assignment (e.g., standard deviation)|
| Lists, iteration | Ability to search data and return all "rows" that match search criteria |
| Lists, iteration | Write the results of a given operation (average, standard deviation) _as a new column_ |
| Conditional logic |	Color-code data presentation (uses the `rich` module) |
| Data types | Automatically convert `int`s in the data _once_ at load-time |
| Data analytics |Create a data plot using the `seaborn` module |

**Make sure to link your issue with the pull request you used to make your actually improvement.**

**If you are not following an improvement suggestion you need to have your improvement suggestion checked by the professor before proceeding.**

## Backup Policy Reminder

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e. weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.