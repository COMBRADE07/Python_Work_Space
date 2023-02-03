# series

# series is representation of 1D array /list
# A Pandas Series is like a column in a table.

import pandas as pd

l1 = [1, 5, 3]
var1 = pd.Series(l1)
print(var1)

# label
# it is some tagged index number by default
print(var1[0])

# create own label
var2 = pd.Series(l1, index=["x", "y", "z"])
print(var2)

# DataFrame
hello_word = {
    "w1": [1, 2, 3],
    "w2": ["Okay", 2, 3],
    "w3": [0, "hey", 2],
    "w4": [1, 2, "boy"]
}

okay_world = pd.DataFrame(hello_word)
print(okay_world)
