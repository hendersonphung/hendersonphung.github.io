---
layout: page
title: COMP 110 Data Analysis
permalink: /comp-110-data-analysis/
---
# Introduction

### The topic at stake for this data analysis project is determining the attitude of students of Spring 2026, COMP 110 on **pre-lecture videos** and **livestream lectures**.


To better understand this, the students across three sections of Spring 2026, COMP 110 took a survey that determined their attitudes.


Furthermore, we took 100 students from each instructors' results to determine attitudes.  


Our sample size will be 200 in total: 
* 100 from Professor Hinks' sections and
* 100 from Professor Lytle's section

***
To start, we will pull the data from the two .CSV files provided via the head function, with N = 100 for both files.

We will then concatenate the data via the concat function.

Then, we will select the relevant columns necessary for our analysis.  This includes columns
* "unc_status"
* "prior_exp"
* "pre_lecture_videos"
* "add_livestream"

{% highlight ruby %}
from tabulate import tabulate
import seaborn as sns
from data_utils import get_keys, convert_columns_to_int, read_csv_rows, column_values, columnar, head, select, concat, count, average_score

DATA_FILE_DIRECTORY: str = "static/data/"
DATA_FILE_NAMES: list[str] = ["survey_izzi.csv", "survey_alyssa.csv"]
DATA_FILE_NAME_IZZI: str = f"{DATA_FILE_DIRECTORY}{DATA_FILE_NAMES[0]}"
DATA_FILE_NAME_ALYSSA: str = f"{DATA_FILE_DIRECTORY}{DATA_FILE_NAMES[1]}"

izzi_data: list[dict[str, str]] = read_csv_rows(DATA_FILE_NAME_IZZI)
alyssa_data: list[dict[str, str]] = read_csv_rows(DATA_FILE_NAME_ALYSSA)

columnar_izzi: dict[str,list[str]] = columnar(izzi_data)
columnar_alyssa: dict[str,list[str]] = columnar(alyssa_data)


izzi_100head: dict[str,list[str]] = head(columnar_izzi, 100)
alyssa_100head: dict[str,list[str]] = head(columnar_alyssa, 100)

combined_100: dict[str,list[str]] = concat(izzi_100head,alyssa_100head)

selected = select(combined_100,["unc_status", "comp_major", "prior_exp", "pre_lecture_videos", "add_livestream"])

tabulate(selected, get_keys(selected), "html")
{% endhighlight %}


| unc_status   | comp_major   | prior_exp                    |   pre_lecture_videos |   add_livestream |
|--------------|--------------|------------------------------|----------------------|------------------|
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
