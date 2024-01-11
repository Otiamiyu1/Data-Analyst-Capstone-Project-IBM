# -*- coding: utf-8 -*-
"""Outlier M3-lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FmRx5LzyfQCCGHmfB1pgg7zG80ZZqHt4

<p style="text-align:center">
    <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>

# **Exploratory Data Analysis Lab**

Estimated time needed: **30** minutes

In this module you get to work with the cleaned dataset from the previous module.

In this assignment you will perform the task of exploratory data analysis.
You will find out the distribution of data, presence of outliers and also determine the correlation between different columns in the dataset.

## Objectives

In this lab you will perform the following:

-   Identify the distribution of data in the dataset.

-   Identify outliers in the dataset.

-   Remove outliers from the dataset.

-   Identify correlation between features in the dataset.

* * *

## Hands on Lab

Import the pandas module.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Load the dataset into a dataframe.

"""

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")

"""## Distribution

### Determine how the data is distributed

The column `ConvertedComp` contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.

This assumes 12 working months and 50 working weeks.

Plot the distribution curve for the column `ConvertedComp`.
"""

# your code goes here
plt.figure(figsize=(12, 6))
sns.kdeplot(df['ConvertedComp'], color='skyblue')
plt.title('Distribution Curve for ConvertedComp')
plt.xlabel('ConvertedComp')
plt.ylabel('Density')
plt.show()

"""Plot the histogram for the column `ConvertedComp`.

"""

# your code goes here
plt.figure(figsize=(12, 6))
sns.histplot(df['ConvertedComp'], bins=30, kde=False, color='skyblue')
plt.title('Histogram for ConvertedComp')
plt.xlabel('ConvertedComp')
plt.ylabel('Frequency')
plt.show()

"""What is the median of the column `ConvertedComp`?

"""

# your code goes here
median_c= df['ConvertedComp'].median()
print(f'median ConvertedComp is {median_c}')

"""How many responders identified themselves only as a **Man**?

"""

# your code goes here
count= df[df['Gender'] == 'Man'].shape[0]
count

"""Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?

"""

# your code goes here
df[df['Gender'] == 'Woman'].median()

"""Give the five number summary for the column `Age`?

**Double click here for hint**.

<!--
min,q1,median,q3,max of a column are its five number summary.
-->
"""

# your code goes here
df['Age'].describe()

"""Plot a histogram of the column `Age`.

"""

# your code goes here
plt.figure(figsize=(12, 6))
sns.histplot(df['Age'], bins=12, kde=False, color='skyblue')
plt.title('Histogram for Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

"""## Outliers

### Finding outliers

Find out if outliers exist in the column `ConvertedComp` using a box plot?
"""

# your code goes here

sns.boxplot(df['ConvertedComp'])
plt.title('Boxplot for ConvertedComp')

plt.show()

"""Find out the Inter Quartile Range for the column `ConvertedComp`.

"""

# your code goes here
Q1 = df['ConvertedComp'].quantile(0.25)
Q3 = df['ConvertedComp'].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1
IQR

"""Find out the upper and lower bounds.

"""

# your code goes here
# Calculate the lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"The lower bound for potential outliers is: {lower_bound}")
print(f"The upper bound for potential outliers is: {upper_bound}")



"""Identify how many outliers are there in the `ConvertedComp` column.

"""

# your code goes here
# Identify outliers
outliers = df[(df['ConvertedComp'] < lower_bound) | (df['ConvertedComp'] > upper_bound)]

# Print the number of outliers
print(f"The number of outliers in the ConvertedComp column is: {len(outliers)}")

"""Create a new dataframe by removing the outliers from the `ConvertedComp` column.

"""

# your code goes here
df_no_outliers = df[(df['ConvertedComp'] >= lower_bound) & (df['ConvertedComp'] <= upper_bound)]

# Print the new DataFrame without outliers
df_no_outliers.head()

df_no_outliers ['ConvertedComp'].median()

df_no_outliers ['ConvertedComp'].mean()

"""## Correlation

### Finding correlation

Find the correlation between `Age` and all other numerical columns.
"""

# your code goes here
correlation_matrix = df_no_outliers .corrwith(df_no_outliers ['Age'])

# Print the correlation between 'Age' and all other numerical columns
print("Correlation between Age and other numerical columns:")
print(correlation_matrix)

"""## Authors

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |

Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
"""