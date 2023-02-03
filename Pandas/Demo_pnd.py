import pandas as pd

datalist = {
    "name": ['Rhutik', 'Vikrant', 'Anup', 'Abhishekh'],
    "marks": [94, 85, 64, 88],
    "city": ['', 'pune', 'akurdi', 'nigdi']
}

df = pd.DataFrame(datalist)
print(df)


