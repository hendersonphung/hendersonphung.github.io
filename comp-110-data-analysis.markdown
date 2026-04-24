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
