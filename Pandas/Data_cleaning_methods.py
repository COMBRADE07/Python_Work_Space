"""
Data Cleaning

Data cleaning means fixing bad data in your data set.

Bad data could be:

   1] Empty cells
   2] Data in wrong format
   3] Wrong data
   4] Duplicates

"""
import pandas as pd

df = pd.read_csv("raw_data_for_cleaning.csv")

# 1] dropna():
#   -used for remove rows those have empty column
#   -By default, the dropna() method returns a new DataFrame, and will not change the original.
#   -If you want to change the original DataFrame, use the inplace = True argument:

new_df = df.dropna()
# df.dropna(inplace = True)
print(new_df.to_string())

# # 2] fillna():  replace in all null values
# #    - used for fill null values
# df2 = pd.read_csv("raw_data_for_cleaning.csv")
# df2.fillna(150, inplace=True)
# print(df2.to_string())
# # 150 will replace in all null values
#
#
# # 3] fill null values in perticular column by targetting perticular column as follows
#
# df['Calories'].fillna(180.22,inplace=True)
# date1 = "14/11/2022"
# df['Date'].fillna(date1,inplace= True)
# print(df.to_string())


# 4] replace using =[    mean    median      mode    ]
df3 = pd.read_csv("raw_data_for_cleaning.csv")
x_mean = df3['Calories'].mean()
x_median = df3['Calories'].median()
x_mode = df3['Calories'].mode()
x_max = df3['Calories'].max()
x_min = df3['Calories'].min()
print("mean", x_mean)
print("median: ", x_median)
print("mode: ", x_mode)
print("max: ", x_max)
print("min: ", x_min)
# df3.fillna(x_mean, inplace=True)
# print(df3.to_string())


# 5] cleaning date format data :
df4 = pd.read_csv("raw_data_for_cleaning.csv")
df4['Date'] = pd.to_datetime(df4['Date'])
print(df4.to_string())


# 6] replacing wrong value to recover wrong data: only for single value
# df.loc(row_number, Column_name) = Value_to_be_set

df5 = pd.read_csv("raw_data_for_cleaning.csv")
df5.loc[7,'Duration']=61
print(df5.to_string())


# 7] duplicate()
'''To discover duplicates, we can use the duplicated() method.

The duplicated() method returns a Boolean values for each row:'''
print(df5.duplicated())


# 8]drop_duplicate():
"""This function will delete duplicate item from the list """
# df.drop_duplicates(inplace= True)
