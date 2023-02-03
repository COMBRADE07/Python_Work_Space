# here we can work with json file
"""Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

In our examples we will be using a JSON file called 'data.json'."""

import pandas as pd

df_js = pd.read_json("json_data.json")

print(df_js)    # this can only print 1st and last 5 rows of file
print(df_js.to_string()) # to print whole data in file


'''
JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.


{
    "duration":{
      '0':80,
      '1':47,
      '2':64
     
    },  
    "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    }
}
'''
