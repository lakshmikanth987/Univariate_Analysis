# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 08:21:50 2020

@author: Lakshmikanth

Titile  :  Univariate Analysis
"""
# Importing the required libraries

import pandas as pd

#Imorting the csv file
data_retirval = pd.read_csv(r"F:\NMIMS\Trimester\Trim - 4\Data Analytics tools & Techniques\Python\Univariate Analysis\Video games\vgsales.csv", encoding='latin-1')

print(data_retirval.columns)

# Bar Chart
data_retirval['Genre'].value_counts().head(10).plot.bar()

# Line chart
data_retirval['Global_Sales'].value_counts().sort_index().head(10).plot.line()

# Area chart
data_retirval['Global_Sales'].value_counts().sort_index().head(10).plot.area()

# Histogram
data_retirval['Global_Sales'].plot.hist()