import pandas as pd

here_we_go = pd.read_csv('info.csv')
print(here_we_go)

# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).

data_x = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data_x,index=['a','b','c'])

print(df.loc['b'])