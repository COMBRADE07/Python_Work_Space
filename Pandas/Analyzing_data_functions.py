# data analyzing functions as follows
"""
1] head():
    - The head() method returns the headers and a specified number of rows, starting from the top.
    - quick overview of the DataFrame
2] tail():
    - The tail() method returns the headers and a specified number of rows, starting from the bottom
    - There is also a tail() method for viewing the last rows of the DataFrame
3] info():
    - The DataFrames object has a method called info(), that gives you more information about the data set.

4] shape:
    - Gives information about total rows and column in data set

5] describe();
    -  The describe() function applies basic statistical computations on the dataset like extreme values,
     count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped.
    - describe() function gives a good picture of the distribution of data.
"""

import pandas as pd

df = pd.read_csv("data_file.csv")



# gets started
print(df.head(20)) # print  1st 20 rows
print(df.tail(5)) # return 5 rows form tail
print(df.info())
print(df.shape)
print(df.describe())

# print(df)
