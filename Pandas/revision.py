from pandas import pandas as pd

# a = [10,20,30,40,50,70,10,20,30]
# store_a = pd.Series(a)
# print(store_a)
#
#
# # index
# # this will set index as mentioned to list a
# storring_a = pd.Series(a,index= ["a","b","c","d","e","f","g","h","i"])
# print(storring_a)
# print(storring_a["c"])
#
# # key/value
#
# hey = {1:"Ram",2:"shyam",3:"Suresh"}
# store_hey = pd.Series(hey)
# print(store_hey)
#
#
# # dataframe
# # shows row and columns
# hie = {"Name":["ramesh","suresh","ganesh","rajesh"],
#        "address":["Chinchwad","Akurdi","Nigdi","Shivajinagar"],
#        "age":[22,23,20,21]}
#
# hie_v = pd.DataFrame(hie)
# print()
# print(hie_v)

# reading csv file
myfile = pd.read_csv("data_file.csv")
# print(myfile)  # this will print 1st and last 5 rows only
# print(myfile.to_string())

# display specific rows
# loc => shows location of index
# print(myfile.loc[0])
# print(myfile.loc[[0, 50, 10, 168]])

# reading json file
# json format
data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "e": 102,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127,
        "z": 155
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300,
        "z": 502
    }
}

# print(data)
# convert json data into dataframe
# df_j = pd.DataFrame(data)
# print(df_j)

# read json file

dff = pd.read_json("json_data.json")

# print(dff)
# print(dff.to_string())
# print(dff.loc[50])
# print(dff.loc[[10, 20, 30, 40, 50, 60, 70]])
# print(dff.head(10))     # print 1st 10 records from file
# print(dff.tail(10))     # print last 10 records from file
# print(dff.info())


# cleaning data set contains following methods
dataf = pd.read_csv("data_file.csv")
new_data = dataf.copy()
# print(new_data.to_string())  # this will return new dataset as result not change original dataset
# this will delete null values column (28 no col)
# new_data.dropna(inplace=True)       # this will change in original data set
# print(new_data.to_string())

# fillna()
# if we don't specify col then it will replace whole dataset

# new_data.fillna(10000,inplace=True)         # set all null value as 10000
# new_data["Calories"].fillna(10000, inplace=True)  # this will only select Calories column

# print(new_data.to_string())


# replace values using mean,median, mode
x_median = new_data["Calories"].median()
x_mean = new_data["Calories"].mean()
x_mode = new_data["Calories"].mode()
# print(new_data.count())     # count not null values

# new_data["Calories"].fillna(x_median,inplace=True)
# print(new_data.to_string())
# print(x_median)
# print(x_mean)
# print(x_mode)



