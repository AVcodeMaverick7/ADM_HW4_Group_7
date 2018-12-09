# HOMEWORK 4 - Group_7
Joanna Broniarek, Vikranth Ale, Matteo  Cavalletti  

The homework consists of two parts:

## 1) Does basic house information reflect house's description?
In this part of the homework our task was to perform a clustering analysis of house announcements in Rome from Immobiliare.it. 
We created two datasets (Information Dataset and Description Dataset) by retrieving data from websites. Then, we used K-mean++ clustering method for both datasets and compared the results. In order to use the best number of clusters per dataset we used Elbow method. At the end, we generated Wordclouds for most similar couples of clusters. 

To perform this analysis we created two notebooks:
+ **Homework4_part1** - main notebook, where most of the analysis is contained
+ **TFIDF_matrix** - notebook for generating TFIDF matrix needed for Description Dataset

Some functions used in analysis was located in the external files :
+ **collect_data.py**
+ **functions.py**

Folder DataFiles contains files created and used during the first part analysis.

## 2) Find the duplicates!
The second part is based on given passwords2.txt file, where each row corresponds to a string of 20 characters. Number of rows in this file is 110 000 000.

The task was to define a hash function that associates a value to each string and check whether there are some duplicate strings or collisions.

The code for this part is located in notebook :
+ **Homework4_part2**
