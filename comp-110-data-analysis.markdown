<!-- ---
layout: page
title: COMP 110 Data Analysis
permalink: /comp-110-data-analysis/
---

Contributors: Henderson Phung, Kyle Bayer

# Introduction

### The topic at stake for this data analysis project is determining the attitude of students of Spring 2026, COMP 110 on **pre-lecture videos** and **livestream lectures**.


To better understand this, the students across three sections of Spring 2026, COMP 110 took a survey that determined their attitudes.


Furthermore, we took 100 students from each instructors' results to determine attitudes.  


Our sample size will be 200 in total: 
* 100 from Professor Hinks' sections and
* 100 from Professor Lytle's section

***

To start, we will pull the data from the two .CSV files provided, select the first 100 students from each section, and concatenate the data via the concat function.

Then, we will select the relevant columns necessary for our analysis.  This includes columns
* "unc_status"
* "prior_exp"
* "pre_lecture_videos"
* "add_livestream"

**Data for analysis**

| unc_status   | comp_major   | prior_exp                    |   pre_lecture_videos |   add_livestream |
|--------------|--------------|------------------------------|---------|---------|
| Senior       | No           | None to less than one month! |                    3 |                5 |
| Sophomore    | No           | 2-6 months                   |                    7 |                6 |
| Freshman     | No           | None to less than one month! |                    4 |                4 |
| Sophomore    | No           | None to less than one month! |                    1 |                2 |
| Sophomore    | No           | None to less than one month! |                    2 |                3 |
| Sophomore    | No           | None to less than one month! |                    7 |                7 |
| Sophomore    | No           | None to less than one month! |                    3 |                3 |
| Junior       | No           | None to less than one month! |                    3 |                5 |
| Sophomore    | Yes - BS     | 2-6 months                   |                    5 |                4 |
| Senior       | No           | 2-6 months                   |                    1 |                5 |
| Junior       | No           | None to less than one month! |                    7 |                6 |
| Freshman     | No           | None to less than one month! |                    7 |                4 |
| Sophomore    | No           | 7-12 months                  |                    7 |                7 |
| Sophomore    | No           | None to less than one month! |                    6 |                5 |
| Senior       | No           | None to less than one month! |                    7 |                4 |
| Sophomore    | No           | 2-6 months                   |                    3 |                7 |
| Junior       | No           | 2-6 months                   |                    3 |                7 |
| Junior       | No           | 2-6 months                   |                    5 |                4 |
| Sophomore    | No           | None to less than one month! |                    7 |                5 |
| Sophomore    | No           | None to less than one month! |                    7 |                7 |
| Sophomore    | No           | 7-12 months                  |                    6 |                7 |
| Sophomore    | No           | 2-6 months                   |                    1 |                1 |
| Junior       | No           | 7-12 months                  |                    5 |                7 |
| Junior       | No           | 1-2 years                    |                    6 |                7 |
| Junior       | No           | None to less than one month! |                    5 |                5 |
| Junior       | Yes - Minor  | None to less than one month! |                    4 |                4 |
| Freshman     | No           | 2-6 months                   |                    4 |                7 |
| Freshman     | No           | None to less than one month! |                    7 |                7 |
| Freshman     | No           | 2-6 months                   |                    5 |                5 |
| Sophomore    | No           | None to less than one month! |                    6 |                6 |
| Senior       | No           | None to less than one month! |                    7 |                7 |
| Junior       | No           | None to less than one month! |                    6 |                4 |
| Sophomore    | No           | 2-6 months                   |                    5 |                4 |
| Junior       | No           | None to less than one month! |                    4 |                7 |
| Senior       | No           | 2-6 months                   |                    3 |                6 |
| Sophomore    | Yes - BS     | 2-6 months                   |                    7 |                7 |
| Sophomore    | No           | 2-6 months                   |                    6 |                7 |
| Freshman     | No           | None to less than one month! |                    5 |                7 |
| Senior       | No           | None to less than one month! |                    7 |                7 |
| Junior       | No           | None to less than one month! |                    5 |                3 |
| Junior       | No           | None to less than one month! |                    4 |                6 |
| Sophomore    | No           | None to less than one month! |                    6 |                6 |
| Sophomore    | No           | None to less than one month! |                    6 |                5 |
| Sophomore    | No           | None to less than one month! |                    6 |                4 |
| Senior       | No           | None to less than one month! |                    5 |                5 |
| Sophomore    | No           | None to less than one month! |                    5 |                5 |
| Senior       | No           | None to less than one month! |                    7 |                5 |
| Senior       | No           | None to less than one month! |                    5 |                6 |
| Senior       | No           | 2-6 months                   |                    4 |                5 |
| Senior       | No           | None to less than one month! |                    6 |                1 |
| Junior       | No           | 2-6 months                   |                    2 |                6 |
| Senior       | No           | None to less than one month! |                    5 |                6 |
| Sophomore    | No           | None to less than one month! |                    4 |                4 |
| Junior       | No           | 2-6 months                   |                    6 |                3 |
| Sophomore    | No           | None to less than one month! |                    5 |                3 |
| Sophomore    | No           | 2-6 months                   |                    4 |                5 |
| Junior       | No           | None to less than one month! |                    3 |                5 |
| Sophomore    | No           | 2-6 months                   |                    1 |                6 |
| Senior       | No           | 2-6 months                   |                    7 |                7 |
| Senior       | No           | None to less than one month! |                    4 |                4 |
| Junior       | No           | None to less than one month! |                    5 |                5 |
| Junior       | No           | None to less than one month! |                    7 |                7 |
| Junior       | No           | 7-12 months                  |                    7 |                7 |
| Senior       | No           | None to less than one month! |                    6 |                6 |
| Senior       | Yes - Minor  | 2-6 months                   |                    6 |                6 |
| Sophomore    | No           | 7-12 months                  |                    4 |                5 |
| Sophomore    | No           | None to less than one month! |                    4 |                5 |
| Sophomore    | No           | None to less than one month! |                    7 |                7 |
| Senior       | No           | None to less than one month! |                    5 |                6 |
| Sophomore    | No           | None to less than one month! |                    5 |                4 |
| Junior       | Yes - BS     | 1-2 years                    |                    7 |                3 |
| Junior       | No           | None to less than one month! |                    7 |                7 |
| Freshman     | No           | None to less than one month! |                    7 |                7 |
| Sophomore    | No           | 2-6 months                   |                    4 |                2 |
| Junior       | No           | None to less than one month! |                    7 |                2 |
| Junior       | No           | 7-12 months                  |                    7 |                5 |
| Junior       | No           | None to less than one month! |                    5 |                5 |
| Junior       | No           | None to less than one month! |                    5 |                5 |
| Junior       | No           | None to less than one month! |                    4 |                4 |
| Senior       | No           | None to less than one month! |                    7 |                7 |
| Senior       | No           | None to less than one month! |                    6 |                5 |
| Sophomore    | No           | None to less than one month! |                    7 |                6 |
| Sophomore    | No           | None to less than one month! |                    3 |                3 |
| Junior       | No           | 2-6 months                   |                    7 |                6 |
| Junior       | No           | None to less than one month! |                    5 |                4 |
| Junior       | No           | None to less than one month! |                    4 |                6 |
| Senior       | No           | 2-6 months                   |                    4 |                4 |
| Sophomore    | No           | 2-6 months                   |                    1 |                3 |
| Junior       | No           | 7-12 months                  |                    6 |                6 |
| Sophomore    | No           | None to less than one month! |                    5 |                5 |
| Sophomore    | Yes - BS     | None to less than one month! |                    5 |                4 |
| Senior       | No           | None to less than one month! |                    5 |                7 |
| Junior       | No           | None to less than one month! |                    7 |                7 |
| Junior       | No           | None to less than one month! |                    6 |                6 |
| Junior       | No           | None to less than one month! |                    1 |                2 |
| Sophomore    | No           | 2-6 months                   |                    6 |                3 |
| Junior       | No           | None to less than one month! |                    5 |                3 |
| Junior       | No           | None to less than one month! |                    5 |                5 |
| Senior       | No           | 7-12 months                  |                    3 |                5 |
| Freshman     | No           | 2-6 months                   |                    7 |                6 |
| Junior       | No           | 1-2 years                    |                    3 |                2 |
| Junior       | No           | 1-2 years                    |                    3 |                5 |
| Sophomore    | No           | None to less than one month! |                    5 |                5 |
| Sophomore    | No           | None to less than one month! |                    7 |                7 |
| Senior       | No           | None to less than one month! |                    4 |                6 |
| Freshman     | No           | 2-6 months                   |                    2 |                1 |
| Sophomore    | No           | None to less than one month! |                    6 |                7 |
| Freshman     | No           | None to less than one month! |                    7 |                7 |
| Sophomore    | No           | None to less than one month! |                    6 |                4 |
| Senior       | No           | 2-6 months                   |                    5 |                5 |
| Sophomore    | No           | None to less than one month! |                    6 |                6 |
| Sophomore    | No           | None to less than one month! |                    6 |                6 |
| Senior       | No           | None to less than one month! |                    4 |                6 |
| Freshman     | No           | None to less than one month! |                    4 |                3 |
| Senior       | No           | None to less than one month! |                    7 |                7 |
| Senior       | No           | 2-6 months                   |                    7 |                7 |
| Senior       | No           | None to less than one month! |                    6 |                5 |
| Sophomore    | No           | None to less than one month! |                    6 |                7 |
| Sophomore    | No           | None to less than one month! |                    6 |                5 |
| Freshman     | No           | None to less than one month! |                    5 |                4 |
| Sophomore    | No           | 2-6 months                   |                    5 |                7 |
| Junior       | No           | None to less than one month! |                    4 |                7 |
| Junior       | No           | None to less than one month! |                    4 |                5 |
| Sophomore    | No           | 2-6 months                   |                    3 |                6 |
| Freshman     | No           | None to less than one month! |                    5 |                2 |
| Junior       | No           | None to less than one month! |                    6 |                7 |
| Sophomore    | No           | None to less than one month! |                    6 |                6 |
| Junior       | No           | 1-2 years                    |                    5 |                5 |
| Sophomore    | No           | None to less than one month! |                    4 |                6 |
| Freshman     | No           | 7-12 months                  |                    3 |                3 |
| Sophomore    | No           | None to less than one month! |                    5 |                4 |
| Sophomore    | No           | None to less than one month! |                    3 |                7 |
| Sophomore    | No           | None to less than one month! |                    5 |                7 |
| Sophomore    | No           | 2-6 months                   |                    5 |                6 |
| Senior       | No           | None to less than one month! |                    4 |                6 |
| Sophomore    | No           | 7-12 months                  |                    2 |                5 |
| Junior       | No           | None to less than one month! |                    6 |                6 |
| Sophomore    | No           | None to less than one month! |                    4 |                6 |
| Senior       | No           | None to less than one month! |                    7 |                4 |
| Junior       | No           | None to less than one month! |                    7 |                2 |
| Senior       | No           | None to less than one month! |                    7 |                7 |
| Senior       | No           | None to less than one month! |                    7 |                7 |
| Sophomore    | No           | 7-12 months                  |                    6 |                7 |
| Senior       | No           | None to less than one month! |                    5 |                7 |
| Sophomore    | No           | 2-6 months                   |                    3 |                7 |
| Sophomore    | No           | 7-12 months                  |                    7 |                7 |
| Sophomore    | No           | Over 2 years                 |                    5 |                5 |
| Sophomore    | No           | 2-6 months                   |                    7 |                7 |
| Sophomore    | No           | 2-6 months                   |                    6 |                7 |
| Junior       | No           | 2-6 months                   |                    6 |                6 |
| Junior       | No           | 1-2 years                    |                    2 |                6 |
| Senior       | No           | None to less than one month! |                    7 |                7 |
| Junior       | No           | 2-6 months                   |                    2 |                7 |
| Junior       | No           | None to less than one month! |                    5 |                1 |
| Sophomore    | No           | None to less than one month! |                    2 |                6 |
| Senior       | No           | 2-6 months                   |                    7 |                7 |
| Sophomore    | Yes - Minor  | 2-6 months                   |                    3 |                7 |
| Freshman     | No           | 2-6 months                   |                    6 |                7 |
| Sophomore    | No           | None to less than one month! |                    7 |                7 |
| Junior       | Yes - Minor  | 2-6 months                   |                    3 |                4 |
| Sophomore    | No           | None to less than one month! |                    7 |                7 |
| Senior       | Yes - Minor  | None to less than one month! |                    6 |                7 |
| Freshman     | No           | 2-6 months                   |                    6 |                5 |
| Sophomore    | No           | 2-6 months                   |                    1 |                7 |
| Sophomore    | No           | None to less than one month! |                    6 |                7 |
| Junior       | No           | None to less than one month! |                    6 |                6 |
| Sophomore    | No           | None to less than one month! |                    5 |                5 |
| Junior       | No           | None to less than one month! |                    6 |                6 |
| Junior       | No           | None to less than one month! |                    7 |                2 |
| Senior       | No           | 2-6 months                   |                    7 |                7 |
| Sophomore    | No           | 2-6 months                   |                    7 |                5 |
| Junior       | No           | None to less than one month! |                    6 |                7 |
| Senior       | No           | None to less than one month! |                    7 |                7 |
| Junior       | No           | None to less than one month! |                    2 |                2 |
| Junior       | No           | 2-6 months                   |                    7 |                3 |
| Junior       | No           | None to less than one month! |                    7 |                7 |
| Freshman     | No           | None to less than one month! |                    6 |                2 |
| Sophomore    | No           | None to less than one month! |                    5 |                6 |
| Sophomore    | No           | None to less than one month! |                    5 |                7 |
| None         | No           | 2-6 months                   |                    4 |                7 |
| Senior       | No           | None to less than one month! |                    7 |                2 |
| Junior       | No           | None to less than one month! |                    7 |                1 |
| Sophomore    | No           | 2-6 months                   |                    3 |                6 |
| Senior       | No           | 1-2 years                    |                    7 |                7 |
| Sophomore    | Yes - BS     | None to less than one month! |                    5 |                6 |
| Junior       | Yes - BS     | 1-2 years                    |                    3 |                7 |
| Sophomore    | Yes - BS     | None to less than one month! |                    7 |                7 |
| Senior       | No           | 2-6 months                   |                    6 |                6 |
| Freshman     | No           | None to less than one month! |                    7 |                7 |
| Sophomore    | No           | None to less than one month! |                    7 |                6 |
| Sophomore    | No           | 2-6 months                   |                    4 |                5 |
| Junior       | Yes - Minor  | 1-2 years                    |                    7 |                7 |
| Sophomore    | No           | 2-6 months                   |                    2 |                2 |
| Sophomore    | No           | 1-2 years                    |                    5 |                5 |
| Freshman     | No           | None to less than one month! |                    7 |                3 |
| Senior       | No           | None to less than one month! |                    6 |                6 |
| Junior       | No           | 2-6 months                   |                    5 |                6 |
| Sophomore    | No           | None to less than one month! |                    1 |                7 |
| Graduate     | No           | None to less than one month! |                    6 |                3 |
| Senior       | No           | None to less than one month! |                    5 |                7 |



### Finding the average scoring on Pre-Lecture Videos and Adding Livestreams

In the survey, the scoring for pre-lecture videos and adding livestreams were on a Likert scale from 1-7, where:
1 being Strongly Disagree and 7 being Strongly Agree.  

By finding averages, we can better understand the average attitude of the 200 students in the sample. 

* For pre-lecture videos, the average score was 5.145 out of 7, indicating a positive attitude toward this implementation.
* For adding livestreams, the average score was 5.345 out of 7, also indicating a positive attitude toward this implementation.

| Column Names       | Average Scores   |
|--------------------|------------------|
| pre_lecture_videos | 5.145 out of 7   |
| add_livestream     | 5.345 out of 7   |



### Tabulating and Bar Graph Visualization of Prior Experiences in Coding and UNC Status
Tabulating the columns Prior Experiences and UNC Status allows to see the count of how many students in each group responded to the survey.  

Furthermore, by doing so, we are able to visualize the populations and representation in the survey.

| Prior Experience             |   count |
|------------------------------|---------|
| None to less than one month! |     125 |
| 2-6 months                   |      52 |
| 7-12 months                  |      12 |
| 1-2 years                    |      10 |
| Over 2 years                 |       1 |

![Prior Experience bar graph](/static/images/prior_experience.png)

| UNC Status   |   count |
|--------------|---------|
| Freshman     |      19 |
| Sophomore    |      78 |
| Junior       |      58 |
| Senior       |      43 |
| Graduate     |       1 |
| None         |       1 |

![UNC Status bar graph](/static/images/unc_status_graph.png)



### Understanding Computer Science major/minors to non-Computer Science majors and their experiences

To get a better understanding of the data, we will need to differentiate Computer Science major/minors to non-Computer Science majors.  

This was done to view experience levels in the class between these two populations.

| Is major/minor   |   count |
|------------------|---------|
| No               |     187 |
| Yes              |      13 |

We will compare the level of experiences between computer science degrees to non-computer science degrees.

![Computer science degrees bar graph](/static/images/unc_status_graph.png)

Here, we see that the majority of students in the class, amongst both populations of computer science degrees have little to no experience in coding.  This is important later to understand the attitudes of pre-lecture videos and adding livestreams.



### Let's analyze the correlation of coding prior experience to attitudes toward pre-lecture videos and adding livestreams.

![Prior Experiences to Attitude on Pre-Lecture Videos](/static/images/attitude_priorexp_to_prelecturevids.png)

We see that majority of non-experience coding students prefer the addition of pre-lecture videos.  The effect of pre-lecture videos will allow these students to get a better understand of what to expect in upcoming lectures.

![Prior Experiences to Attitude on Adding Livestreams](/static/images/attitude_priorexp_to_addlivestream.png)

We see that a majority of the students surveyed, across all experience levels, prefer the implementation of livestreams to the course.



### Conclusion

In our findings, we better understood the population of our sample (n = 200) and their attitudes toward adding pre-lecture videos and livestream elements to the course.

We saw that a majority of the students in the course are sophomores and juniors, and have no experience coding.

Within the population, we saw that there is support for adding both pre-lecture videos and livestreams to the count, as the Likert scale averages for these questions were:

| Implementing       | Average Scores   |
|--------------------|------------------|
| pre_lecture_videos | 5.145 out of 7   |
| add_livestream     | 5.345 out of 7   |

The effect of pre-lecture videos will allow these students to get a better understand of what to expect in upcoming lectures and to have the ability to review introductory concepts of new topics.  This is especially crucial for the large amount of no-experience coders in the course.

The effect of adding livestreams to the course will allow students to rewatch lectures at their own convenience to better grasp material covered in class, including practice problems and concept explanations provided by the instructor.  Furthermore, livestreams will allow students to remotely attend class, however, the attendance policy should be changed if implementing this as this will affect attendance rates during the semester.  

Overall, implementing livestreams is a benefit for attending students across all experience levels to be able to review, recall, and retrive information covered in lectures and is a great tool for active learning. -->
